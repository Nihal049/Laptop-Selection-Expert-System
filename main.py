import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

from knowledge_base import (
    BUDGET_OPTIONS,
    USAGE_OPTIONS,
    RAM_OPTIONS,
    STORAGE_OPTIONS,
    GRAPHICS_OPTIONS,
    RULES
)
from inference_engine import run_inference


def format_rule_for_display(rule):
    lines = [rule["id"], ""]
    first = True
    order = ["usage", "graphics", "ram", "storage", "budget"]
    sorted_keys = sorted(
        rule["conditions"].keys(),
        key=lambda k: order.index(k) if k in order else 99
    )

    for key in sorted_keys:
        value = rule["conditions"][key]
        field_name = "RAM" if key == "ram" else key.capitalize()
        val_str = " or ".join(value) if isinstance(value, (list, tuple)) else str(value)
        prefix = "IF" if first else "AND"
        lines.append(f"{prefix} {field_name} = {val_str}")
        first = False

    lines.append(f"THEN Recommendation = {rule['recommendation']}")
    return "\n".join(lines)


def get_rule_by_id(rule_id):
    for rule in RULES:
        if rule.get("id") == rule_id:
            return rule
    return None


class LaptopExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Laptop Selection Expert System")
        self.root.geometry("1100x700")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#F1F5F9")

        self.c_bg = "#F1F5F9"
        self.c_card = "#FFFFFF"
        self.c_header = "#1E3A8A"
        self.c_text_dark = "#0F172A"
        self.c_text_muted = "#64748B"
        self.c_text_body = "#334155"
        self.c_border = "#E2E8F0"
        self.c_primary = "#2563EB"
        self.c_primary_hover = "#1D4ED8"
        self.c_reset = "#64748B"
        self.c_reset_hover = "#475569"
        self.c_kb = "#0F766E"
        self.c_kb_hover = "#115E59"

        self._configure_styles()
        self._build_header()
        self._build_main_layout()

    def _configure_styles(self):
        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except Exception:
            pass

        self.style.configure(
            "TCombobox",
            font=("Segoe UI", 10),
            padding=5,
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            foreground=self.c_text_dark,
            bordercolor=self.c_border,
            lightcolor=self.c_border,
            darkcolor=self.c_border
        )
        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#FFFFFF")],
            selectbackground=[("readonly", "#EFF6FF")],
            selectforeground=[("readonly", self.c_text_dark)]
        )

    def _build_header(self):
        header_frame = tk.Frame(self.root, bg=self.c_header, padx=28, pady=16)
        header_frame.pack(fill="x", side="top")

        title_lbl = tk.Label(
            header_frame,
            text="Laptop Selection Expert System",
            font=("Segoe UI", 16, "bold"),
            bg=self.c_header,
            fg="#FFFFFF"
        )
        title_lbl.pack(anchor="w")

        subtitle_lbl = tk.Label(
            header_frame,
            text="Find the right laptop category using a rule-based expert system.",
            font=("Segoe UI", 10),
            bg=self.c_header,
            fg="#BFDBFE"
        )
        subtitle_lbl.pack(anchor="w", pady=(3, 0))

    def _build_main_layout(self):
        main_container = tk.Frame(self.root, bg=self.c_bg, padx=24, pady=20)
        main_container.pack(fill="both", expand=True)

        main_container.columnconfigure(0, weight=4, minsize=420)
        main_container.columnconfigure(1, weight=5, minsize=500)
        main_container.rowconfigure(0, weight=1)

        left_card = tk.Frame(
            main_container,
            bg=self.c_card,
            highlightbackground=self.c_border,
            highlightthickness=1,
            padx=24,
            pady=22
        )
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        left_title = tk.Label(
            left_card,
            text="Your Requirements",
            font=("Segoe UI", 13, "bold"),
            bg=self.c_card,
            fg=self.c_text_dark
        )
        left_title.pack(anchor="w", pady=(0, 16))

        self.var_budget = tk.StringVar(value="-- Select Budget --")
        self.var_usage = tk.StringVar(value="-- Select Usage --")
        self.var_ram = tk.StringVar(value="-- Select RAM --")
        self.var_storage = tk.StringVar(value="-- Select Storage --")
        self.var_graphics = tk.StringVar(value="-- Select Graphics --")

        self._add_input_field(left_card, "1. Budget", self.var_budget, BUDGET_OPTIONS)
        self._add_input_field(left_card, "2. Primary Usage", self.var_usage, USAGE_OPTIONS)
        self._add_input_field(left_card, "3. RAM Requirement", self.var_ram, RAM_OPTIONS)
        self._add_input_field(left_card, "4. Storage Requirement", self.var_storage, STORAGE_OPTIONS)
        self._add_input_field(left_card, "5. Graphics Requirement", self.var_graphics, GRAPHICS_OPTIONS)

        btn_recommend_frame = tk.Frame(left_card, bg=self.c_card)
        btn_recommend_frame.pack(fill="x", pady=(20, 10))

        self.btn_recommend = tk.Button(
            btn_recommend_frame,
            text="Get Recommendation",
            font=("Segoe UI", 10, "bold"),
            bg=self.c_primary,
            fg="#FFFFFF",
            activebackground=self.c_primary_hover,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=10,
            command=self.handle_get_recommendation
        )
        self.btn_recommend.pack(fill="x")
        self._bind_button_hover(self.btn_recommend, self.c_primary, self.c_primary_hover)

        btn_sub_frame = tk.Frame(left_card, bg=self.c_card)
        btn_sub_frame.pack(fill="x")

        self.btn_reset = tk.Button(
            btn_sub_frame,
            text="Reset",
            font=("Segoe UI", 9, "bold"),
            bg=self.c_reset,
            fg="#FFFFFF",
            activebackground=self.c_reset_hover,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=8,
            command=self.handle_reset
        )
        self.btn_reset.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._bind_button_hover(self.btn_reset, self.c_reset, self.c_reset_hover)

        self.btn_kb = tk.Button(
            btn_sub_frame,
            text="View Knowledge Base",
            font=("Segoe UI", 9, "bold"),
            bg=self.c_kb,
            fg="#FFFFFF",
            activebackground=self.c_kb_hover,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=8,
            command=self.show_knowledge_base_window
        )
        self.btn_kb.pack(side="right", fill="x", expand=True, padx=(6, 0))
        self._bind_button_hover(self.btn_kb, self.c_kb, self.c_kb_hover)

        right_card = tk.Frame(
            main_container,
            bg=self.c_card,
            highlightbackground=self.c_border,
            highlightthickness=1,
            padx=26,
            pady=22
        )
        right_card.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

        right_title = tk.Label(
            right_card,
            text="Laptop Recommendation",
            font=("Segoe UI", 13, "bold"),
            bg=self.c_card,
            fg=self.c_text_dark
        )
        right_title.pack(anchor="w", pady=(0, 16))

        self.right_body = tk.Frame(right_card, bg=self.c_card)
        self.right_body.pack(fill="both", expand=True)

        self._show_empty_state()

    def _add_input_field(self, parent, label_text, var, options):
        field_frame = tk.Frame(parent, bg=self.c_card)
        field_frame.pack(fill="x", pady=(0, 10))

        lbl = tk.Label(
            field_frame,
            text=label_text,
            font=("Segoe UI", 9, "bold"),
            bg=self.c_card,
            fg=self.c_text_body
        )
        lbl.pack(anchor="w", pady=(0, 4))

        combo = ttk.Combobox(
            field_frame,
            textvariable=var,
            values=options,
            state="readonly",
            font=("Segoe UI", 10)
        )
        combo.pack(fill="x")
        return combo

    def _bind_button_hover(self, btn, normal_color, hover_color):
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=normal_color))

    def _show_empty_state(self):
        for widget in self.right_body.winfo_children():
            widget.destroy()

        empty_box = tk.Frame(self.right_body, bg=self.c_card)
        empty_box.pack(fill="both", expand=True)

        empty_center = tk.Frame(empty_box, bg=self.c_card)
        empty_center.pack(expand=True)

        empty_msg = tk.Label(
            empty_center,
            text="Choose your requirements and click\nGet Recommendation",
            font=("Segoe UI", 12),
            bg=self.c_card,
            fg=self.c_text_muted,
            justify="center"
        )
        empty_msg.pack()

    def handle_get_recommendation(self):
        selected = {
            "budget": self.var_budget.get(),
            "usage": self.var_usage.get(),
            "ram": self.var_ram.get(),
            "storage": self.var_storage.get(),
            "graphics": self.var_graphics.get()
        }

        missing = []
        if selected["budget"].startswith("--"):
            missing.append("Budget")
        if selected["usage"].startswith("--"):
            missing.append("Primary Usage")
        if selected["ram"].startswith("--"):
            missing.append("RAM Requirement")
        if selected["storage"].startswith("--"):
            missing.append("Storage Requirement")
        if selected["graphics"].startswith("--"):
            missing.append("Graphics Requirement")

        if missing:
            msg = "Please select all requirements before getting a recommendation:\n\n• " + "\n• ".join(missing)
            messagebox.showwarning("Missing Requirements", msg, parent=self.root)
            return

        result = run_inference(selected)
        self._display_recommendation(result)

    def _display_recommendation(self, result):
        for widget in self.right_body.winfo_children():
            widget.destroy()

        user_inputs = result["user_inputs"]
        category = result["category"]
        reason = result["reason"]
        rule_id = result["matched_rule_id"]
        is_fallback = result.get("is_fallback", False)

        container = tk.Frame(self.right_body, bg=self.c_card)
        container.pack(fill="both", expand=True)

        cat_section = tk.Frame(container, bg=self.c_card)
        cat_section.pack(fill="x", pady=(0, 12))

        cat_tag = tk.Label(
            cat_section,
            text="RECOMMENDED CATEGORY",
            font=("Segoe UI", 8, "bold"),
            bg=self.c_card,
            fg=self.c_primary
        )
        cat_tag.pack(anchor="w")

        cat_title = tk.Label(
            cat_section,
            text=category,
            font=("Segoe UI", 16, "bold"),
            bg=self.c_card,
            fg=self.c_header
        )
        cat_title.pack(anchor="w", pady=(2, 0))

        why_section = tk.Frame(container, bg=self.c_card)
        why_section.pack(fill="x", pady=(0, 12))

        why_lbl = tk.Label(
            why_section,
            text="Why this was recommended",
            font=("Segoe UI", 10, "bold"),
            bg=self.c_card,
            fg=self.c_text_dark
        )
        why_lbl.pack(anchor="w", pady=(0, 3))

        why_content = tk.Label(
            why_section,
            text=reason,
            font=("Segoe UI", 9),
            bg="#F8FAFC",
            fg=self.c_text_body,
            justify="left",
            wraplength=480,
            padx=10,
            pady=8,
            relief="solid",
            bd=1,
            highlightbackground=self.c_border
        )
        why_content.pack(fill="x")

        req_section = tk.Frame(container, bg=self.c_card)
        req_section.pack(fill="x", pady=(0, 12))

        req_lbl = tk.Label(
            req_section,
            text="YOUR REQUIREMENTS",
            font=("Segoe UI", 8, "bold"),
            bg=self.c_card,
            fg=self.c_text_muted
        )
        req_lbl.pack(anchor="w", pady=(0, 4))

        req_grid = tk.Frame(
            req_section,
            bg="#F8FAFC",
            relief="solid",
            bd=1,
            highlightbackground=self.c_border,
            padx=12,
            pady=8
        )
        req_grid.pack(fill="x")

        req_grid.columnconfigure(0, weight=1)
        req_grid.columnconfigure(1, weight=2)

        items = [
            ("Budget", user_inputs["budget"]),
            ("Usage", user_inputs["usage"]),
            ("RAM", user_inputs["ram"]),
            ("Storage", user_inputs["storage"]),
            ("Graphics", user_inputs["graphics"])
        ]

        for i, (k, v) in enumerate(items):
            k_lbl = tk.Label(
                req_grid,
                text=k,
                font=("Segoe UI", 8, "bold"),
                bg="#F8FAFC",
                fg=self.c_text_muted,
                anchor="w"
            )
            k_lbl.grid(row=i, column=0, sticky="w", pady=1)

            v_lbl = tk.Label(
                req_grid,
                text=v,
                font=("Segoe UI", 8),
                bg="#F8FAFC",
                fg=self.c_text_dark,
                anchor="w"
            )
            v_lbl.grid(row=i, column=1, sticky="w", pady=1, padx=(10, 0))

        rule_section = tk.Frame(container, bg=self.c_card)
        rule_section.pack(fill="x")

        rule_lbl = tk.Label(
            rule_section,
            text="Rule Applied",
            font=("Segoe UI", 10, "bold"),
            bg=self.c_card,
            fg=self.c_text_dark
        )
        rule_lbl.pack(anchor="w", pady=(0, 4))

        rule_obj = get_rule_by_id(rule_id)
        if rule_obj:
            rule_text = format_rule_for_display(rule_obj)
        elif is_fallback:
            rule_text = (
                "FALLBACK RULE\n\n"
                f"IF Usage = {user_inputs['usage']}\n"
                f"AND Budget = {user_inputs['budget']}\n"
                f"THEN Recommendation = {category}"
            )
        else:
            rule_text = f"{rule_id}\n\nTHEN Recommendation = {category}"

        rule_box = tk.Label(
            rule_section,
            text=rule_text,
            font=("Consolas", 8),
            bg="#F8FAFC",
            fg=self.c_text_body,
            justify="left",
            anchor="w",
            padx=10,
            pady=8,
            relief="solid",
            bd=1,
            highlightbackground=self.c_border
        )
        rule_box.pack(fill="x")

    def handle_reset(self):
        self.var_budget.set("-- Select Budget --")
        self.var_usage.set("-- Select Usage --")
        self.var_ram.set("-- Select RAM --")
        self.var_storage.set("-- Select Storage --")
        self.var_graphics.set("-- Select Graphics --")
        self._show_empty_state()

    def set_inputs_and_recommend(self, budget, usage, ram, storage, graphics):
        self.var_budget.set(budget)
        self.var_usage.set(usage)
        self.var_ram.set(ram)
        self.var_storage.set(storage)
        self.var_graphics.set(graphics)
        self.handle_get_recommendation()

    def show_knowledge_base_window(self):
        kb_win = tk.Toplevel(self.root)
        kb_win.title("Knowledge Base - IF-THEN Rules")
        kb_win.geometry("760x650")
        kb_win.minsize(640, 500)
        kb_win.configure(bg=self.c_bg)

        top_bar = tk.Frame(kb_win, bg=self.c_header, padx=20, pady=14)
        top_bar.pack(fill="x", side="top")

        kb_title = tk.Label(
            top_bar,
            text="Knowledge Base - IF-THEN Rules",
            font=("Segoe UI", 13, "bold"),
            bg=self.c_header,
            fg="#FFFFFF"
        )
        kb_title.pack(anchor="w")

        kb_sub = tk.Label(
            top_bar,
            text=f"Total Rules Loaded: {len(RULES)} | Expert System Rules",
            font=("Segoe UI", 9),
            bg=self.c_header,
            fg="#BFDBFE"
        )
        kb_sub.pack(anchor="w", pady=(2, 0))

        search_frame = tk.Frame(kb_win, bg=self.c_bg, padx=20, pady=10)
        search_frame.pack(fill="x")

        search_lbl = tk.Label(
            search_frame,
            text="Filter rules:",
            font=("Segoe UI", 9, "bold"),
            bg=self.c_bg,
            fg=self.c_text_body
        )
        search_lbl.pack(side="left", padx=(0, 8))

        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, font=("Segoe UI", 9))
        search_entry.pack(side="left", fill="x", expand=True)

        text_frame = tk.Frame(kb_win, bg="#FFFFFF", padx=20, pady=6)
        text_frame.pack(fill="both", expand=True)

        txt_rules = scrolledtext.ScrolledText(
            text_frame,
            wrap="word",
            font=("Consolas", 10),
            bg="#FAFAFA",
            fg=self.c_text_dark,
            relief="solid",
            bd=1,
            padx=12,
            pady=12
        )
        txt_rules.pack(fill="both", expand=True)

        def populate_rules(filter_text=""):
            txt_rules.config(state="normal")
            txt_rules.delete("1.0", tk.END)

            filter_lower = filter_text.strip().lower()
            matching_count = 0
            divider = "\n" + ("-" * 64) + "\n\n"

            for i, rule in enumerate(RULES):
                rule_display = format_rule_for_display(rule)
                if not filter_lower or (filter_lower in rule_display.lower()) or (filter_lower in rule["id"].lower()):
                    matching_count += 1
                    txt_rules.insert(tk.END, rule_display + "\n")
                    if i < len(RULES) - 1:
                        txt_rules.insert(tk.END, divider)

            if matching_count == 0:
                txt_rules.insert(tk.END, f"No rules matched filter '{filter_text}'.\n")

            txt_rules.config(state="disabled")

        populate_rules()
        search_var.trace_add("write", lambda *args: populate_rules(search_var.get()))

        btm_bar = tk.Frame(kb_win, bg=self.c_bg, padx=20, pady=12)
        btm_bar.pack(fill="x", side="bottom")

        close_btn = tk.Button(
            btm_bar,
            text="Close",
            font=("Segoe UI", 9, "bold"),
            bg=self.c_reset,
            fg="#FFFFFF",
            activebackground=self.c_reset_hover,
            activeforeground="#FFFFFF",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=6,
            command=kb_win.destroy
        )
        close_btn.pack(side="right")
        self._bind_button_hover(close_btn, self.c_reset, self.c_reset_hover)


def main():
    root = tk.Tk()
    app = LaptopExpertSystemApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
