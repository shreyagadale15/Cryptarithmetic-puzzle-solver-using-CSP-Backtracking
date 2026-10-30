from flask import Flask, render_template, request
from solver import solve_cryptarithm, parse_puzzle, word_to_number

app = Flask(__name__)

PRESETS = [
    "SEND + MORE = MONEY",
    "TWO + TWO = FOUR",
    "EAT + THAT = APPLE",
    "CROSS + ROADS = DANGER",
    "BASE + BALL = GAMES",
]

@app.route("/", methods=["GET", "POST"])
def index():
    puzzle = "SEND + MORE = MONEY"
    use_pruning = True
    count_all = False
    result = None
    error = None

    if request.method == "POST":
        puzzle = request.form.get("puzzle", "").upper().strip()
        use_pruning = request.form.get("pruning") == "on"
        count_all = request.form.get("all_solutions") == "on"
        try:
            solutions = solve_cryptarithm(
                puzzle,
                use_pruning=use_pruning,
                all_solutions=count_all
            )
            addends, result_word, _, _ = parse_puzzle(puzzle)
            result = {
                "solutions": solutions,
                "count": len(solutions),
                "puzzle": puzzle,
                "addends": addends,
                "result_word": result_word,
                "numeric_equations": [
                    {
                        "left": [word_to_number(word, solution) for word in addends],
                        "right": word_to_number(result_word, solution)
                    }
                    for solution in solutions
                ]
            }
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "index.html",
        puzzle=puzzle,
        presets=PRESETS,
        use_pruning=use_pruning,
        count_all=count_all,
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
