# Cryptarithmetic Puzzle Solver using CSP Backtracking

A Python and Flask web application that solves addition-based cryptarithmetic puzzles. Each distinct letter is assigned a unique digit (0–9), and leading letters cannot be zero.

## Features

- CSP representation using variables, domains, and constraints
- Recursive backtracking search
- Column-wise arithmetic checking (pruning)
- Preset puzzles and custom puzzle input
- Option to stop after the first solution or find all solutions
- Browser-based interface

## Example

Puzzle:

```text
  SEND
+ MORE
------
 MONEY
```

One valid solution:

```text
S=9, E=5, N=6, D=7
M=1, O=0, R=8, Y=2

9567 + 1085 = 10652
```

## Project structure

```text
Cryptarithmetic_Puzzle_Solver_GitHub/
├── app.py
├── solver.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run locally

1. Install Python 3.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\\Scripts\\activate
   ```

   macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the local address shown in the terminal (usually `http://127.0.0.1:5000`).

## Puzzle format

Use uppercase or lowercase letters with addition and one equals sign:

```text
WORD + WORD = RESULT
```

The solver currently supports addition puzzles with one or more addends.

## GitHub upload

Create a new repository on GitHub. Upload the files and folders in this project, or push them using Git:

```bash
git init
git add .
git commit -m "Add cryptarithmetic CSP backtracking solver"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.

## Algorithm overview

1. Parse the addends and result word.
2. Identify unique letters and leading letters.
3. Assign unused digits to letters.
4. Check each arithmetic column from right to left, including carry.
5. Backtrack when a digit assignment violates a constraint.
6. Display the valid letter-to-digit mapping.

## Technologies

- Python 3
- Flask
- HTML
- CSS
- JavaScript

## Academic project

Prepared as a Foundation of Artificial Intelligence mini project: **Cryptarithmetic Puzzle Solver using CSP Backtracking**.
