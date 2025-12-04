# benchmark/benchmark_kmp.py
# Simple benchmark for KMP emotional search.

import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")

if SRC not in sys.path:
    sys.path.append(SRC)

from search_engine import SearchEngine  # type: ignore


def main():
    print("=== KMP Benchmark ===")

    engine = SearchEngine(
        lyrics_dir=os.path.join(ROOT, "data", "lyrics"),
        emotions_path=os.path.join(ROOT, "data", "emotions.json"),
        labels_path=os.path.join(ROOT, "data", "labels.json")
    )

    engine.load_lyrics()

    start = time.perf_counter()
    engine.compute_counts()
    end = time.perf_counter()

    elapsed = end - start
    num_songs = len(engine.songs)
    throughput = num_songs / elapsed if elapsed > 0 else 0

    print(f"Processed: {num_songs} songs")
    print(f"Total time: {elapsed:.4f} seconds")
    print(f"Throughput: {throughput:.2f} songs/sec")

    # Save result
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    out_path = os.path.join(ROOT, "results", "benchmarks.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"Processed: {num_songs} songs\n")
        f.write(f"Total time: {elapsed:.4f} seconds\n")
        f.write(f"Throughput: {throughput:.2f} songs/sec\n")

    print(f"\nBenchmark saved to results/benchmarks.txt")


if __name__ == "__main__":
    main()
