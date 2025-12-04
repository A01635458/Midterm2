# plotter.py
import os
import json
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_sa_curve(history, outdir):
    plt.figure(figsize=(10,5))
    plt.plot(history)
    plt.title("Simulated Annealing Cost Curve")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{outdir}/sa_cost_curve.png")
    plt.close()


def plot_emotion_counts(emotions, lyrics_dir, outdir):
    from collections import Counter
    total_counts = Counter()

    for path in glob.glob(f"{lyrics_dir}/*.txt"):
        text = open(path, encoding="utf-8").read().lower()
        for emotion, words in emotions.items():
            for w in words:
                total_counts[emotion] += text.count(w)

    plt.figure(figsize=(10,5))
    plt.bar(total_counts.keys(), total_counts.values(), color="skyblue")
    plt.title("Total Emotional Word Counts")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{outdir}/emotion_counts.png")
    plt.close()


def plot_heatmap(emotions, lyrics_dir, outdir):
    rows = []
    names = []

    for path in sorted(glob.glob(f"{lyrics_dir}/*.txt")):
        song = path.split("/")[-1]
        names.append(song)

        text = open(path, encoding="utf-8").read().lower()
        row = []
        for em, words in emotions.items():
            row.append(sum(text.count(w) for w in words))
        rows.append(row)

    df = pd.DataFrame(rows, columns=emotions.keys(), index=names)

    plt.figure(figsize=(12,8))
    sns.heatmap(df, cmap="YlGnBu", annot=True, fmt="d")
    plt.title("Emotion Heatmap Across Songs")
    plt.tight_layout()
    plt.savefig(f"{outdir}/emotion_heatmap.png")
    plt.close()


def plot_top10(engine, emotions, outdir):
    for emotion in emotions.keys():
        rank = engine.score(emotion)

        songs = [r[0] for r in rank[:10]]
        scores = [r[1] for r in rank[:10]]

        plt.figure(figsize=(8,5))
        plt.barh(songs, scores, color="lightgreen")
        plt.gca().invert_yaxis()
        plt.title(f"Top 10 '{emotion}' Songs")
        plt.xlabel("Score")
        plt.tight_layout()
        plt.savefig(f"{outdir}/top10_{emotion}.png")
        plt.close()
