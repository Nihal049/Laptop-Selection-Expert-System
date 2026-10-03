"""
=============================================================================
Automated Test Suite for Laptop Selection Expert System
=============================================================================
Verifies:
1. Knowledge base loading and rule counts.
2. Inference engine rule matching for all 5 user test cases.
3. Conflict resolution specificity.
4. Fallback recommendation handling.
5. Rule text formatting for GUI display.
=============================================================================
"""

import sys
import io

# Ensure UTF-8 output encoding for Windows consoles that default to cp1252
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

from knowledge_base import RULES, get_all_rules_text, format_rule
from inference_engine import run_inference


def test_test_cases():
    print("=" * 70)
    print("RUNNING AUTOMATED TEST CASES")
    print("=" * 70)

    test_cases = [
        {
            "name": "Test Case 1 (Basic / Office Work, Entry Budget)",
            "inputs": {
                "budget": "Below ₹40,000",
                "usage": "Basic / Office Work",
                "ram": "8 GB",
                "storage": "256 GB SSD",
                "graphics": "Integrated Graphics"
            },
            "expected_category": "Basic Student / Office Laptop",
            "expected_rule": "RULE 1"
        },
        {
            "name": "Test Case 2 (Programming / Development, Mid-Range)",
            "inputs": {
                "budget": "₹40,000 - ₹60,000",
                "usage": "Programming / Development",
                "ram": "16 GB",
                "storage": "512 GB SSD",
                "graphics": "Integrated Graphics"
            },
            "expected_category": "Programming / Mid-Range Laptop",
            "expected_rule": "RULE 2"
        },
        {
            "name": "Test Case 3 (Gaming, Dedicated Graphics, 60k-80k)",
            "inputs": {
                "budget": "₹60,000 - ₹80,000",
                "usage": "Gaming",
                "ram": "16 GB",
                "storage": "512 GB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Mid-Range Gaming Laptop",
            "expected_rule": "RULE 4"
        },
        {
            "name": "Test Case 4 (Video Editing, Dedicated GPU, 60k-80k)",
            "inputs": {
                "budget": "₹60,000 - ₹80,000",
                "usage": "Video Editing",
                "ram": "16 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Video Editing / Creator Laptop",
            "expected_rule": "RULE 6"
        },
        {
            "name": "Test Case 5 (Video Editing, 32GB RAM, Flagship Budget)",
            "inputs": {
                "budget": "Above ₹1,00,000",
                "usage": "Video Editing",
                "ram": "32 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Professional Creator Laptop",
            "expected_rule": "RULE 7"
        },
        {
            "name": "Test Case 6 (Student / Multitasking, 16GB, 512GB)",
            "inputs": {
                "budget": "₹40,000 - ₹60,000",
                "usage": "Student / Multitasking",
                "ram": "16 GB",
                "storage": "512 GB SSD",
                "graphics": "Integrated Graphics"
            },
            "expected_category": "Student Productivity Laptop",
            "expected_rule": "RULE 8"
        },
        {
            "name": "Test Case 7 (Video Editing + Integrated Graphics, High Budget/RAM)",
            "inputs": {
                "budget": "Above ₹1,00,000",
                "usage": "Video Editing",
                "ram": "32 GB",
                "storage": "1 TB SSD",
                "graphics": "Integrated Graphics"
            },
            "expected_category": "Basic Video Editing Laptop",
            "expected_rule": "RULE 17"
        },
        {
            "name": "Case A (Above 1L, Gaming, 8GB RAM, Dedicated GPU)",
            "inputs": {
                "budget": "Above ₹1,00,000",
                "usage": "Gaming",
                "ram": "8 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Gaming Laptop - RAM Upgrade Recommended",
            "expected_rule": "RULE 26"
        },
        {
            "name": "Case B (Above 1L, Gaming, 16GB RAM, Dedicated GPU)",
            "inputs": {
                "budget": "Above ₹1,00,000",
                "usage": "Gaming",
                "ram": "16 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "High Performance Gaming Laptop",
            "expected_rule": "RULE 25"
        },
        {
            "name": "Case C (Above 1L, Gaming, 32GB RAM, Dedicated GPU)",
            "inputs": {
                "budget": "Above ₹1,00,000",
                "usage": "Gaming",
                "ram": "32 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Enthusiast / Flagship Gaming Laptop",
            "expected_rule": "RULE 12"
        },
        {
            "name": "Case D - RULE 27 (Below 40k, Gaming, 32GB RAM, 1TB SSD, Dedicated GPU)",
            "inputs": {
                "budget": "Below ₹40,000",
                "usage": "Gaming",
                "ram": "32 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Budget Insufficient for Selected Gaming Requirements",
            "expected_rule": "RULE 27"
        },
        {
            "name": "Case E - RULE 28 (Below 40k, Gaming, 32GB RAM, 512GB SSD, Dedicated GPU)",
            "inputs": {
                "budget": "Below ₹40,000",
                "usage": "Gaming",
                "ram": "32 GB",
                "storage": "512 GB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Budget Insufficient / Reduce RAM Requirement",
            "expected_rule": "RULE 28"
        },
        {
            "name": "Case F - RULE 29 (Below 40k, Gaming, 16GB RAM, 1TB SSD, Dedicated GPU)",
            "inputs": {
                "budget": "Below ₹40,000",
                "usage": "Gaming",
                "ram": "16 GB",
                "storage": "1 TB SSD",
                "graphics": "Dedicated Graphics"
            },
            "expected_category": "Budget Insufficient / Review Storage Requirement",
            "expected_rule": "RULE 29"
        }
    ]

    all_passed = True

    for tc in test_cases:
        print(f"\nEvaluating: {tc['name']}")
        result = run_inference(tc["inputs"])
        print(f"  Inputs: {tc['inputs']}")
        print(f"  Result Category: {result['category']}")
        print(f"  Matched Rule: {result['matched_rule_id']} (Specificity: {result['specificity']})")
        print(f"  Reason: {result['reason'][:120]}...")

        # Assertions
        assert result["category"] == tc["expected_category"], (
            f"Expected {tc['expected_category']}, got {result['category']}"
        )
        assert result["matched_rule_id"] == tc["expected_rule"], (
            f"Expected rule {tc['expected_rule']}, got {result['matched_rule_id']}"
        )
        print("  -> PASSED [OK]")

    # Knowledge Base checks
    print("\n" + "=" * 70)
    print("VERIFYING KNOWLEDGE BASE FORMATTING")
    print("=" * 70)
    rules_text = get_all_rules_text()
    assert len(RULES) >= 20, f"Expected >= 20 rules, found {len(RULES)}"
    assert "IF Usage = Gaming" in rules_text
    assert "THEN Recommendation = Mid-Range Gaming Laptop" in rules_text
    print(f"Total Rules loaded: {len(RULES)}")
    print("Sample Formatted Rule output:")
    print("-" * 40)
    print(format_rule(RULES[3]))
    print("-" * 40)
    print("Knowledge base format verification: PASSED [OK]")

    print("\n" + "=" * 70)
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    test_test_cases()
