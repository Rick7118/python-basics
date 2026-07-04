# Python Basics

A set of small, self-contained scripts I wrote while revising Python fundamentals. Each file covers one concept and is meant to be read top to bottom, then run and tinkered with.

Useful if you already know how to program in another language (Java, C, JS, etc.) and just want to see Python's syntax and idioms quickly, without a full beginner course.

## What's in here

| File | Covers |
|---|---|
| `01_print.py` | `print()`, string concatenation |
| `02_variables.py` | Variable types (str, int, float, bool, tuple, list, set, dict), type conversion, type annotations, f-strings |
| `03_functions.py` | Function definitions, type hints, default arguments |
| `04_looping.py` | `for` loops (over ranges and lists), `while` loops |
| `05_controflowlogic.py` | `if`/`elif`/`else`, a minimal rule-based chatbot loop |
| `06_errorhandling.py` | `try`/`except` basics |
| `07_imports.py` | Import styles: full module, aliased, selective (`from ... import ...`) |
| `08_project.py` | Small combined project — a slightly more capable chatbot with basic arithmetic and input validation |

## How to use this

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-basics.git
   cd python-basics
   ```
2. Make sure you have Python 3.9+ installed:
   ```bash
   python --version
   ```
3. Run any file directly to see it in action:
   ```bash
   python 01_print.py
   ```
4. Open the file alongside the output to see what each line did. Files are numbered in the order I'd recommend going through them — each one builds slightly on the last.
5. Change things. Break things. That's the actual point — reading code you already half-understand teaches you less than editing it and seeing what breaks.

## Suggested order for someone new to Python

1. `01_print.py` → `02_variables.py` — syntax and data types
2. `03_functions.py` → `04_looping.py` → `05_controflowlogic.py` — control flow and reusable code
3. `06_errorhandling.py` — handling bad input gracefully
4. `07_imports.py` — using Python's standard library
5. `08_project.py` — see it all combined into one small interactive program

## Notes

These are revision scripts, not production code — some are intentionally simple to isolate one concept at a time. If you spot something to improve, feel free to open a PR.