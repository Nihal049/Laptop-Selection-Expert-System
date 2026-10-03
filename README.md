Laptop Selection Expert System
Project Overview

The Laptop Selection Expert System is a simple rule-based application that recommends a suitable laptop category based on the user's requirements.

The user provides details such as:

Budget
Primary usage
RAM
Storage
Graphics

The system checks these requirements against predefined IF-THEN rules and gives a suitable laptop recommendation.

The project works completely offline and does not require an internet connection, database, or external API.

Objective

The main objective of this project is to create a simple expert system that can help users select a suitable laptop category based on their requirements and budget.

Features
Simple graphical user interface using Tkinter
Budget-based laptop recommendations
Recommendations based on different usage types
RAM, storage, and graphics requirements
Rule-based decision making
29 predefined rules
Handles specific combinations of requirements
Provides a fallback recommendation when no specific rule matches
Shows the rule applied for the recommendation
Provides an explanation for the recommendation
View Knowledge Base option to see the available rules
Reset option to clear the current selection
Works completely offline
How the System Works

The system follows this flow:

User Input
    ↓
Knowledge Base
    ↓
Inference Engine
    ↓
Matching Rules
    ↓
Laptop Recommendation
    ↓
Explanation

The user selects the required laptop specifications from the interface.

The inference engine checks the selected values against the rules in the knowledge base.

If multiple rules match, the system selects the more specific rule.

If no specific rule matches, a general fallback rule provides a recommendation.

Knowledge Base

The knowledge base contains 29 IF-THEN rules.

Each rule checks conditions such as:

Budget
Primary usage
RAM
Storage
Graphics

Example:

IF usage = Gaming
AND graphics = Dedicated Graphics
AND RAM = 32 GB
AND budget = Above ₹1L
THEN recommend Enthusiast / Flagship Gaming Laptop

The rules are stored in knowledge_base.py.

Inference Engine

The inference engine is responsible for finding the appropriate recommendation.

It uses forward chaining to compare the user's input with the conditions of the rules.

When more than one rule matches, the system uses the number of matching conditions to select the more specific rule.

If a specific rule is not available, a general rule or fallback rule is used.

The inference logic is implemented in inference_engine.py.

Project Structure
laptop-selection-expert-system/
│
├── main.py
├── knowledge_base.py
├── inference_engine.py
├── test_system.py
├── test_gui.py
├── requirements.txt
└── README.md
main.py

Contains the Tkinter graphical interface of the application.

knowledge_base.py

Contains the IF-THEN rules used by the expert system.

inference_engine.py

Contains the logic used to match user requirements with the rules.

test_system.py

Contains tests for the rule matching and recommendation system.

test_gui.py

Contains tests related to the GUI.

requirements.txt

Contains the project dependency information.

README.md

Contains the project information and instructions.

Technologies Used
Python
Tkinter
Rule-Based Expert System
Forward Chaining

No external database or API is required.

How to Run
1. Install Python

Install Python on your computer if it is not already installed.

2. Open the Project Folder

Open a terminal or command prompt inside the project folder.

3. Run the Application
python main.py

The Laptop Selection Expert System window will open.

How to Use
Select your budget.
Select your primary usage.
Select the required RAM.
Select the required storage.
Select the required graphics type.
Click Get Recommendation.
The system will display the recommended laptop category.
The applied rule and explanation will also be displayed.

Use Reset to clear the current selections.

Use View Knowledge Base to view the rules used by the system.

Example

For example, if the user selects:

Budget: Above ₹1L
Usage: Gaming
RAM: 32 GB
Storage: 1 TB SSD
Graphics: Dedicated Graphics

The system checks the matching rules and can recommend:

Enthusiast / Flagship Gaming Laptop

The application also displays the rule that was applied and an explanation for the recommendation.

Special Cases

The system also handles cases where the selected requirements may not be suitable for the selected budget.

For example, a gaming laptop with very high RAM, large storage, and dedicated graphics with a very low budget can result in a message indicating that the budget is insufficient for the selected requirements.

Testing

To test the rule-based system, run:

python test_system.py

To test the GUI, run:

python test_gui.py

The tests check whether the system produces the expected results for different combinations of requirements.

Notes
The system provides laptop categories rather than specific laptop brands or models.
Recommendations are based on the rules defined in the knowledge base.
The application works offline.
No internet connection is required to use the application.
No database is required.
The rules can be modified or extended in knowledge_base.py.