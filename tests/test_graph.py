# tests/test_graph.py
# Tests for EmotionalGraph.

import os
import sys
import json

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
DATA = os.path.join(ROOT, "data")
if SRC not in sys.path:
    sys.path.append(SRC)

from emotional_graph import EmotionalGraph


def test_graph_scoring():
    # Create minimal emotions.json for test
    emotions_path = os.path.join(DATA, "emotions_test.json")
    os.makedirs(DATA, exist_ok=True)

    with open(emotions_path, "w", encoding="utf-8") as f:
        json.dump({"joy": ["happy", "smile"]}, f)

    graph = EmotionalGraph(emotions_path)

    counts = {"happy": 3, "smile": 1}
    score = graph.score_counts_for_emotion("joy", counts)

    assert score > 0, "Score should be > 0"
    print("✔ EmotionalGraph scoring test passed.")


def test_graph_weights_change():
    emotions_path = os.path.join(DATA, "emotions_test.json")

    graph = EmotionalGraph(emotions_path)
    old = graph.get_weight("joy", "happy")

    graph.set_weight("joy", "happy", old + 2.0)
    new = graph.get_weight("joy", "happy")

    assert new > old, "Weight should increase"
    print("✔ EmotionalGraph weight-change test passed.")


if __name__ == "__main__":
    test_graph_scoring()
    test_graph_weights_change()
    print("ALL EMOTIONAL GRAPH TESTS PASSED")
