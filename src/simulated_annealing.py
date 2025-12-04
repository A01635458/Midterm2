# simulated_annealing.py
# Simple SA optimizer for emotional weights.

import os
import json
import random
import math
from typing import Dict, List, Tuple
from emotional_graph import EmotionalGraph


class SimulatedAnnealingOptimizer:
    def __init__(self, graph: EmotionalGraph, song_counts: Dict[str, Dict[str, int]], labels_path: str):
        self.graph = graph
        self.song_counts = song_counts
        self.labels = self._load_labels(labels_path)

    def _load_labels(self, path: str) -> Dict[str, str]:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        print("[SA] No labels.json found (optional). Using dummy cost.")
        return {}

    def _predict(self, counts: Dict[str, int]) -> str:
        scores = self.graph.score_counts_all(counts)
        return max(scores.items(), key=lambda x: x[1])[0]

    def _cost(self) -> float:
        if not self.labels:
            # Dummy cost: lower cost = higher total score
            total = 0
            for counts in self.song_counts.values():
                for e in self.graph.get_emotions():
                    total += self.graph.score_counts_for_emotion(e, counts)
            return -total

        errors = 0
        for song, counts in self.song_counts.items():
            if song in self.labels:
                if self._predict(counts) != self.labels[song]:
                    errors += 1
        return float(errors)

    def _perturb(self) -> List[Tuple[str, str, float]]:
        changes = []
        for _ in range(3):
            e = random.choice(self.graph.get_emotions())
            w = random.choice(self.graph.get_words_for_emotion(e))
            old = self.graph.get_weight(e, w)
            new = max(0.0, old + random.uniform(-0.3, 0.3))
            self.graph.set_weight(e, w, new)
            changes.append((e, w, old))
        return changes

    def _undo(self, changes: List[Tuple[str, str, float]]) -> None:
        for e, w, old in changes:
            self.graph.set_weight(e, w, old)

    def optimize(self, max_iters: int = 200) -> Tuple[float, float]:
        temp = 5.0
        cost = self._cost()
        best = cost

        print(f"[SA] Initial cost: {cost:.4f}")

        for _ in range(max_iters):
            if temp < 0.1:
                break

            changes = self._perturb()
            new_cost = self._cost()
            delta = new_cost - cost

            if delta < 0 or random.random() < math.exp(-delta / temp):
                cost = new_cost
                if new_cost < best:
                    best = new_cost
            else:
                self._undo(changes)

            temp *= 0.97

        print(f"[SA] Final cost: {best:.4f}")
        return cost, best
