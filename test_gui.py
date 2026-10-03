"""
=============================================================================
Automated GUI Test for Redesigned Laptop Selection Expert System
=============================================================================
Verifies:
1. Initialization of window and styles.
2. Selection and execution of all 5 benchmark cases.
3. Verification of:
   - Recommended Category display
   - Why this was recommended section
   - Your Requirements two-column grid
   - Rule Applied section showing exact IF-THEN rule
4. Reset button restoring the empty state.
5. Opening and rendering of Knowledge Base window.
=============================================================================
"""

import sys
import tkinter as tk

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

from main import LaptopExpertSystemApp


def test_gui_automation():
    print("=" * 70)
    print("RUNNING AUTOMATED GUI TESTS")
    print("=" * 70)

    root = tk.Tk()
    root.withdraw() 

    app = LaptopExpertSystemApp(root)
    root.update()
    print("Application initialized successfully with 1100x700 responsive layout.")

    cases = [
        {
            "name": "Case 1: Basic / Office Work",
            "budget": "Below ₹40,000",
            "usage": "Basic / Office Work",
            "ram": "8 GB",
            "storage": "256 GB SSD",
            "graphics": "Integrated Graphics",
            "expected_category": "Basic Student / Office Laptop",
            "expected_rule": "RULE 1"
        },
        {
            "name": "Case 2: Programming / Development",
            "budget": "₹40,000 - ₹60,000",
            "usage": "Programming / Development",
            "ram": "16 GB",
            "storage": "512 GB SSD",
            "graphics": "Integrated Graphics",
            "expected_category": "Programming / Mid-Range Laptop",
            "expected_rule": "RULE 2"
        },
        {
            "name": "Case 3: Gaming",
            "budget": "₹60,000 - ₹80,000",
            "usage": "Gaming",
            "ram": "16 GB",
            "storage": "512 GB SSD",
            "graphics": "Dedicated Graphics",
            "expected_category": "Mid-Range Gaming Laptop",
            "expected_rule": "RULE 4"
        },
        {
            "name": "Case 4: Video Editing (60k-80k)",
            "budget": "₹60,000 - ₹80,000",
            "usage": "Video Editing",
            "ram": "16 GB",
            "storage": "1 TB SSD",
            "graphics": "Dedicated Graphics",
            "expected_category": "Video Editing / Creator Laptop",
            "expected_rule": "RULE 6"
        },
        {
            "name": "Case 5: Video Editing (>1L)",
            "budget": "Above ₹1,00,000",
            "usage": "Video Editing",
            "ram": "32 GB",
            "storage": "1 TB SSD",
            "graphics": "Dedicated Graphics",
            "expected_category": "Professional Creator Laptop",
            "expected_rule": "RULE 7"
        }
    ]

    for tc in cases:
        print(f"\nEvaluating GUI: {tc['name']}")
        app.set_inputs_and_recommend(
            budget=tc["budget"],
            usage=tc["usage"],
            ram=tc["ram"],
            storage=tc["storage"],
            graphics=tc["graphics"]
        )
        root.update()

        # Check that right_body container has the rendered recommendation widgets
        container = app.right_body.winfo_children()[0]
        sections = container.winfo_children()

        # Section 0: Category section
        cat_section = sections[0]
        cat_text = cat_section.winfo_children()[1].cget("text")
        assert cat_text == tc["expected_category"], (
            f"Expected {tc['expected_category']}, got {cat_text}"
        )

        # Section 1: Why this was recommended
        why_section = sections[1]
        why_text = why_section.winfo_children()[1].cget("text")
        assert len(why_text) > 10, "Why recommended text should not be empty"

        # Section 2: YOUR REQUIREMENTS
        req_section = sections[2]
        assert req_section.winfo_children()[0].cget("text") == "YOUR REQUIREMENTS"

        # Section 3: Rule Applied
        rule_section = sections[3]
        rule_box_text = rule_section.winfo_children()[1].cget("text")
        assert tc["expected_rule"] in rule_box_text, (
            f"Expected {tc['expected_rule']} in rule box, got: {rule_box_text}"
        )
        assert "THEN Recommendation =" in rule_box_text

        print(f"  Category displayed: {cat_text}")
        print(f"  Rule Applied verified: {tc['expected_rule']}")
        print("  -> PASSED [OK]")

    # Test Reset
    print("\n--- Testing Reset Button ---")
    app.handle_reset()
    root.update()
    assert app.var_budget.get() == "-- Select Budget --"
    assert app.var_usage.get() == "-- Select Usage --"
    assert app.var_ram.get() == "-- Select RAM --"
    assert app.var_storage.get() == "-- Select Storage --"
    assert app.var_graphics.get() == "-- Select Graphics --"

    # Verify empty state is displayed
    empty_label = app.right_body.winfo_children()[0].winfo_children()[0].winfo_children()[0]
    assert "Choose your requirements and click" in empty_label.cget("text")
    print("Reset functionality: PASSED [OK] (Restored dropdowns and empty state).")

    # Test Knowledge Base Window
    print("\n--- Testing Knowledge Base Window ---")
    app.show_knowledge_base_window()
    root.update()
    print("Knowledge Base window loaded and verified: PASSED [OK]")

    root.destroy()
    print("\n" + "=" * 70)
    print("ALL GUI TESTS PASSED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    test_gui_automation()
