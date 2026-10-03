from knowledge_base import RULES


def condition_matches(rule_value, user_value):
    if isinstance(rule_value, (list, tuple, set)):
        return user_value in rule_value
    return user_value == rule_value


def generate_explanation(rule, user_inputs):
    conditions = rule.get("conditions", {})
    parts = []

    if "usage" in conditions:
        parts.append(f"usage is {user_inputs.get('usage')}")
    if "budget" in conditions:
        parts.append(f"budget is {user_inputs.get('budget')}")
    if "graphics" in conditions:
        parts.append(f"graphics is {user_inputs.get('graphics')}")
    if "ram" in conditions:
        parts.append(f"RAM is {user_inputs.get('ram')}")
    if "storage" in conditions:
        parts.append(f"storage is {user_inputs.get('storage')}")

    if not parts:
        conditions_text = "inputs match the rule criteria"
    elif len(parts) == 1:
        conditions_text = parts[0]
    elif len(parts) == 2:
        conditions_text = f"{parts[0]}, and your {parts[1]}"
    else:
        conditions_text = ", your ".join(parts[:-1]) + f", and your {parts[-1]}"

    rationale = rule.get("rationale", "")
    rule_id = rule.get("id", "RULE")
    recommendation = rule.get("recommendation", "Standard Laptop")

    return (
        f"Your selected {conditions_text}. "
        f"Based on the expert-system rules ({rule_id}), a {recommendation} category is recommended.\n\n"
        f"Reasoning Details: {rationale}"
    )


def get_fallback_recommendation(user_inputs):
    usage = user_inputs.get("usage", "Basic / Office Work")
    budget = user_inputs.get("budget", "₹40,000 - ₹60,000")
    graphics = user_inputs.get("graphics", "Integrated Graphics")

    fallback_map = {
        "Gaming": {
            "category": "Balanced Gaming Laptop",
            "reason": (
                f"Your selected usage is Gaming with a budget of {budget}. "
                f"While no single rule matched all inputs, a Balanced Gaming Laptop is recommended "
                f"to ensure sufficient graphics processing and thermal capacity for gaming workloads."
            )
        },
        "Video Editing": {
            "category": "Multimedia Creator Laptop",
            "reason": (
                f"Your selected usage is Video Editing with a budget of {budget}. "
                f"A Multimedia Creator Laptop is recommended to balance multi-threaded rendering "
                f"performance and high memory capacity within your specified budget."
            )
        },
        "Programming / Development": {
            "category": "General Purpose Developer Laptop",
            "reason": (
                f"Your selected usage is Programming / Development with a budget of {budget}. "
                f"A General Purpose Developer Laptop is recommended to comfortably run development tools, "
                f"code editors, and local runtime environments."
            )
        },
        "Student / Multitasking": {
            "category": "All-Rounder Student Laptop",
            "reason": (
                f"Your selected usage is Student / Multitasking with a budget of {budget}. "
                f"An All-Rounder Student Laptop is recommended for balanced battery life, portability, "
                f"and smooth productivity."
            )
        },
        "Basic / Office Work": {
            "category": "Everyday Office Laptop",
            "reason": (
                f"Your selected usage is Basic / Office Work with a budget of {budget}. "
                f"An Everyday Office Laptop is recommended to reliably handle spreadsheets, documents, "
                f"and web conferencing."
            )
        }
    }

    fallback_info = fallback_map.get(
        usage,
        {
            "category": "General Purpose Laptop",
            "reason": (
                f"A general-purpose laptop is recommended to accommodate your primary usage of "
                f"'{usage}' within your '{budget}' budget."
            )
        }
    )

    return {
        "category": fallback_info["category"],
        "reason": (
            f"Note: Evaluated via inference fallback mechanism.\n"
            f"{fallback_info['reason']}"
        ),
        "matched_rule_id": "FALLBACK RULE",
        "matched_conditions": {"usage": usage, "budget": budget, "graphics": graphics},
        "specificity": 1,
        "is_fallback": True,
        "user_inputs": user_inputs
    }


class InferenceEngine:
    def __init__(self, rules=None):
        self.rules = rules if rules is not None else RULES

    def infer(self, user_inputs):
        matching_rules = []

        for rule in self.rules:
            conditions = rule.get("conditions", {})
            all_conditions_satisfied = True

            for key, expected_value in conditions.items():
                user_value = user_inputs.get(key)
                if not condition_matches(expected_value, user_value):
                    all_conditions_satisfied = False
                    break

            if all_conditions_satisfied:
                specificity = len(conditions)
                matching_rules.append((specificity, rule))

        if matching_rules:
            matching_rules.sort(key=lambda item: item[0], reverse=True)
            best_specificity, best_rule = matching_rules[0]

            explanation = generate_explanation(best_rule, user_inputs)
            return {
                "category": best_rule["recommendation"],
                "reason": explanation,
                "matched_rule_id": best_rule["id"],
                "matched_conditions": best_rule["conditions"],
                "specificity": best_specificity,
                "is_fallback": False,
                "user_inputs": user_inputs
            }

        return get_fallback_recommendation(user_inputs)


inference_engine = InferenceEngine()


def run_inference(user_inputs):
    return inference_engine.infer(user_inputs)
