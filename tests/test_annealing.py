# tests/test_annealing.py
# Basic test for the Simulated Annealing optimizer.

import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
DATA = os.path.join(ROOT, "data")

if SRC not in sys.path:
    sys.path.append(SRC)

from emotional_graph import EmotionalGraph
from simulated_annealing import SimulatedAnnealingOptimizer


def test_annealing_runs():
    # Create fake emotions.json
    emotions_path = os.path.join(DATA, "emotions_test2.json")
    os.makedirs(DATA, exist_ok=True)

    with open(emotions_path, "w", encoding="utf-8") as f:
        json.dump({"sadness": ["cry", "tears"]}, f)

    # Fake word counts for 2 songs
    counts = {
        "song1.txt": {"cry": 3},
        "song2.txt": {"tears": 1}
    }

    # Fake labels
    labels_path = os.path.join(DATA, "labels_test.json")
    with open(labels_path, "w", encoding="utf-8") as f:
        json.dump({"song1.txt": "sadness", "song2.txt": "sadness"}, f)

    graph = EmotionalGraph(emotions_path)
    optimizer = SimulatedAnnealingOptimizer(graph, counts, labels_path)
    c0, cf = optimizer.optimize(max_iters=30)

    assert cf <= c0, "Final cost should be <= initial cost"
    print("✔ Simulated Annealing basic test passed.")


if __name__ == "__main__":
    test_annealing_runs()
    print(" ALL ANNEALING TESTS PASSED")
