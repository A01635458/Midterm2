#main.py

import os
import sys
import time

CURRENT = os.path.dirname(__file__)
if CURRENT not in sys.path:
    sys.path.append(CURRENT)

from search_engine import SearchEngine

from plotter import (
    plot_sa_curve,
    plot_emotion_counts,
    plot_heatmap,
    plot_top10
)

import json


def main():
    engine = SearchEngine(
        lyrics_dir="data/lyrics",
        emotions_path="data/emotions.json",
        labels_path="data/labels.json"
    )

    print("------Emotion-Aware Lyric Search Engine----")

    engine.load_lyrics()

    print("\n[1] Benchmarking KMP...")
    t, thr = engine.benchmark()
    print(f"Time: {t:.4f}s | Throughput: {thr:.2f} songs/s")

    print("\n[2] Running Simulated Annealing...")
    start = time.perf_counter()
    engine.optimize()
    end = time.perf_counter()
    print(f"Optimization time: {end - start:.4f}s")
    engine.compute_counts()

    #lista de emociones
    emotions = list(engine.graph.emotion_to_words.keys())

    print("\n[3] Ranking songs for ALL emotions")
    os.makedirs("results", exist_ok=True)
    plots_dir = "results/plots"
    os.makedirs(plots_dir, exist_ok=True)

    #guardar y print
    with open("results/scores.txt", "w", encoding="utf-8") as f:

        for emotion in emotions:
            print(f"\n Emotion: {emotion.upper()}")
            f.write(f"\n {emotion.upper()} \n")

            results = engine.score(emotion)

            for i, (song, score, matches) in enumerate(results[:10], start=1):
                line = f"{i}. {song} | score={score:.3f} | matches={matches}"
                print(line)
                f.write(line + "\n")

    print("\n[4] Generating plots...")

    with open("data/emotions.json") as f:
        emotions_dict = json.load(f)

    #SA cost curve
    plot_sa_curve(engine.optimizer.history, plots_dir)

    #emotion word counts
    plot_emotion_counts(emotions_dict, "data/lyrics", plots_dir)

    #emotion heatmap
    plot_heatmap(emotions_dict, "data/lyrics", plots_dir)

    #top10 por emotion
    plot_top10(engine, emotions_dict, plots_dir)

    print("\nAll plots saved in results/plots/")
    print("Done.")


if __name__ == "__main__":
    main()
