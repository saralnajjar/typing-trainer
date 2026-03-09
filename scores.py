import json
import os

SCORES_FILE = os.path.join(os.path.dirname(__file__), "scores.json")


def load_scores() -> list:
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_score(result: dict, difficulty: str) -> None:
    scores = load_scores()
    scores.append({
        "wpm": result["wpm"],
        "accuracy": result["accuracy"],
        "elapsed": result["elapsed"],
        "difficulty": difficulty,
    })
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def show_high_scores() -> None:
    scores = load_scores()
    if not scores:
        print("\n  No scores yet. Complete a test to get started!\n")
        return

    print("\n" + "─" * 60)
    print(f"  {'DIFFICULTY':<12} {'WPM':<10} {'ACCURACY':<12} {'TIME (s)'}")
    print("─" * 60)

    sorted_scores = sorted(scores, key=lambda s: s["wpm"], reverse=True)
    for s in sorted_scores[:10]:
        print(f"  {s['difficulty']:<12} {s['wpm']:<10} {s['accuracy']:<12} {s['elapsed']}")

    print("─" * 60)
    print(f"  Personal best: {sorted_scores[0]['wpm']} WPM\n")
