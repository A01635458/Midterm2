# main.py
# Main entry. Runs the whole system.

import os
import sys
import time

CURRENT = os.path.dirname(__file__)
if CURRENT not in sys.path:
    sys.path.append(CURRENT)

from search_engine import SearchEngine


def main():
    engine = SearchEngine(
        lyrics_dir="data/lyrics",
        emotions_path="data/emotions.json",
        labels_path="data/labels.json"
    )

    print("=== Emotion-Aware Lyric Search Engine ===")

    engine.load_lyrics()

    print("\n[1] Benchmarking KMP...")
    t, thr = engine.benchmark()
    print(f"Time: {t:.4f}s | Throughput: {thr:.2f} songs/s")

    print("\n[2] Running Simulated Annealing...")
    start = time.perf_counter()
    engine.optimize()
    end = time.perf_counter()
    print(f"Optimization time: {end - start:.4f}s")

    target = "nostalgia"
    print(f"\n[3] Ranking songs for emotion: '{target}'")
    results = engine.score(target)

    for i, (song, score, matches) in enumerate(results[:10]):
        print(f"{i+1}. {song} | score={score:.3f} | matches={matches}")

    os.makedirs("results", exist_ok=True)
    with open("results/scores.txt", "w", encoding="utf-8") as f:
        for (song, score, matches) in results:
            f.write(f"{song}\t{score:.4f}\t{matches}\n")

    print("\nScores saved to results/scores.txt")


if __name__ == "__main__":
    main()
