cat > scores.py << 'EOF'
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


def show_stats() -> None:
    scores = load_scores()
    if not scores:
        print("\n  No scores yet. Complete a test to get started!\n")
        return

    print("\n" + "═" * 60)
    print("  STATS")
    print("═" * 60)

    # overall
    all_wpm = [s["wpm"] for s in scores]
    all_acc = [s["accuracy"] for s in scores]
    avg_wpm = round(sum(all_wpm) / len(all_wpm), 1)
    avg_acc = round(sum(all_acc) / len(all_acc), 1)
    best_wpm = max(all_wpm)

    print(f"\n  Sessions:      {len(scores)}")
    print(f"  Average WPM:   {avg_wpm}")
    print(f"  Best WPM:      {best_wpm}")
    print(f"  Average Acc:   {avg_acc}%")

    # trend: compare last 5 vs previous 5
    if len(scores) >= 6:
        recent = scores[-5:]
        previous = scores[-10:-5]
        recent_avg = round(sum(s["wpm"] for s in recent) / len(recent), 1)
        previous_avg = round(sum(s["wpm"] for s in previous) / len(previous), 1)
        diff = round(recent_avg - previous_avg, 1)
        trend = f"↑ +{diff}" if diff > 0 else f"↓ {diff}" if diff < 0 else "→ no change"
        print(f"\n  Trend (last 5 vs previous 5): {trend} WPM")

    # per difficulty
    print("\n  " + "─" * 56)
    print(f"  {'DIFFICULTY':<12} {'SESSIONS':<12} {'AVG WPM':<12} {'BEST WPM'}")
    print("  " + "─" * 56)
    for diff in ["Easy", "Medium", "Hard"]:
        subset = [s for s in scores if s["difficulty"] == diff]
        if subset:
            a = round(sum(s["wpm"] for s in subset) / len(subset), 1)
            b = max(s["wpm"] for s in subset)
            print(f"  {diff:<12} {len(subset):<12} {a:<12} {b}")

    print("═" * 60 + "\n")
EOF