# 🧰 MyPyModules – Python CLI + PyQt5 Utilities Toolkit

![Python 3.7+](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Project Type: CLI %2B GUI](https://img.shields.io/badge/Project-CLI%20%2B%20GUI-green)

---

This project contains several useful Python modules I've created to speed up development for CLI tools, GUI apps, and educational quizzes. Each folder serves a specific purpose — organized under `MyLibrary`, `MyMath`, `MyQuiz`, and `MyQt5`.

---

## 💡 Why I Built This

As a self-taught developer exploring Python, PyQt5, and command-line development, I often found myself rewriting the same bits of code — input validation, menu systems, number utilities, and basic widgets.

I built **MyPyModules** as a personal toolkit to:
- Reduce repetitive coding,
- Practice clean and modular programming,
- And reuse well-tested logic across different projects.

It started as a learning project and gradually evolved into a helpful utility set for both CLI and GUI programs. While originally built using Python 3.7.4, most modules are compatible with Python 3.7+.

---

## 🚀 Getting Started

No installation is needed — just clone the repo and import the modules you need.

```bash
git clone https://github.com/Umairccodes/MyPyModules.git
cd MyPyModules

Example imports:

from MyLibrary.input_validators import validate_number
from MyMath.calculate import list_sum
from MyQuiz.framework import MCQ
from MyQt5.MyLabel import ClickableLabel

📁 Project Structure

MyLibrary/
├── input_validators.py     # User input validation helpers for numbers and choices
├── menu.py                 # Dynamic and user-friendly CLI menu system

MyMath/
├── calculate.py            # General-purpose arithmetic calculation functions
├── decimal.py              # Precision-safe decimal operations
├── fractions.py            # Fraction operations and formatting
├── hcf_lcm.py              # Utilities to compute HCF and LCM

MyQt5/
├── __init__.py             # Qt5 module initializer
├── MyButton.py             # Custom QPushButton with added behavior
├── MyLabel.py              # Interactive QLabel components

MyQuiz/
├── framework.py            # Class-based MCQ logic
├── mcq_template.py         # Template functions to run complete quizzes

🔍 About the Modules
🧮 MyLibrary – Core CLI Helpers

A collection of reusable building blocks for CLI applications.
🧪 input_validators.py

Robust input validation functions:

    validate_choice(prompt, options)
    Ensures the user selects a valid option from a list (case-insensitive).

    validate_number(...)
    Prompts for numeric input with control over:

        Type (int or float)

        Range (min_val, max_val)

        Length constraints (e.g. number of digits)

        Inclusive/exclusive bounds

    Perfect for CLI tools that require strict input handling.

📜 menu.py

A simple but flexible Menu class for console-based menus.

Features:

    Optional menu title

    Auto-numbered options

    Optional Exit/Back option

    Input validated using validate_number()

Example:

from MyLibrary.menu import Menu

menu = Menu(["Start", "Settings"], "Main Menu")
choice = menu.display_menu()

🧮 MyMath – Handy Math Functions
➕ calculate.py

Basic arithmetic operations on iterable inputs:

    list_product(iterable)

    list_sum(iterable)

    list_subtraction(iterable)

    list_divide(iterable) (safe division, handles zero)

Returns default values for empty inputs (0 for sum, 1 for product, etc.).
🔢 decimal.py

    isValid_decimal(prompt)
    Repeatedly prompts until a valid float is entered using input() + exception handling.

🧮 fractions.py

    isValid_fraction(prompt) – Accepts input like "3/4" and validates format

    simplify_fraction(num, den) – Returns simplified result (e.g. 6/8 → 3/4)

    handle_negative_denominator(num, den) – Ensures denominator is positive

Example:

from MyMath.fractions import isValid_fraction, simplify_fraction

num, den = isValid_fraction("Enter a fraction: ")
print("Simplified:", simplify_fraction(num, den))

📐 hcf_lcm.py

    gcd(a, b) – Calculates Greatest Common Divisor (using Euclidean algorithm)

    lcm(a, b) – Calculates Least Common Multiple via: (a * b) // gcd(a, b)

🎨 MyQt5 – Custom Qt5 Widgets

Lightweight PyQt5 widgets that speed up GUI creation.
🔘 MyButton.py

    MyButton
    Subclass of QPushButton with a default pointing hand cursor.

Example:

from MyQt5.MyButton import MyButton

btn = MyButton("Click Me")

🏷️ MyLabel.py

    ClickableLabel
    Subclass of QLabel that emits signals on left/right mouse clicks:

        leftClicked

        rightClicked

Example:

from MyQt5.MyLabel import ClickableLabel

label = ClickableLabel("Click me")
label.leftClicked.connect(lambda: print("Left click!"))
label.rightClicked.connect(lambda: print("Right click!"))

❓ MyQuiz – MCQ-Based Quiz Framework

A clean, reusable way to run multiple-choice quizzes in the terminal.
🎓 framework.py

Defines the MCQ class:

    Randomizes answer options

    Validates user input

    Tracks correct answers

    Shows the correct answer when the user is wrong

Example:

from MyQuiz.framework import MCQ

q1 = MCQ(
    "What is the capital of France?",
    {1: "Paris", 2: "Berlin", 3: "Rome", 4: "Madrid"},
    1
)
q1.ask_question()

🧪 mcq_template.py

Utilities to run full quizzes.

Functions:

    ask_questions(questions) – Asks each MCQ, returns score

    show_score(score, total) – Nicely formatted result

    quiz(questions, show_result=True) – Combines all steps

Example:

from MyQuiz.framework import MCQ
from MyQuiz.mcq_template import quiz

questions = [
    MCQ("What is 2+2?", {1: "3", 2: "4", 3: "5"}, 2),
    MCQ("Which planet is red?", {1: "Earth", 2: "Mars", 3: "Jupiter"}, 2)
]

quiz(questions)

✅ Great for learning tools, coding practice, or quick quiz apps.
📄 License

This project is licensed under the MIT License – see the LICENSE file for details.