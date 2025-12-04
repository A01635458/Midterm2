# search_engine.py
# Loads lyrics, runs KMP, builds word counts, scores emotions.

import os
import glob
import time
from typing import Dict, List, Tuple

from trie import Trie
from kmp import kmp_search
from emotional_graph import EmotionalGraph
from simulated_annealing import SimulatedAnnealingOptimizer


class SearchEngine:
    def __init__(self, lyrics_dir: str, emotions_path: str, labels_path: str):
        self.lyrics_dir = lyrics_dir
        self.graph = EmotionalGraph(emotions_path)
        self.labels_path = labels_path

        self.songs: Dict[str, str] = {}
        self.trie = Trie()

        self.word_counts: Dict[str, Dict[str, int]] = {}
        self.optimizer: SimulatedAnnealingOptimizer | None = None   # <-- NEW

    def load_lyrics(self) -> None:
        files = sorted(glob.glob(os.path.join(self.lyrics_dir, "song*.txt")))
        for f in files:
            song_id = os.path.basename(f)
            text = open(f, "r", encoding="utf-8").read()
            self.songs[song_id] = text
            self.trie.insert_text(text)
        print(f"[Engine] Loaded {len(self.songs)} songs.")

    def _count_words(self, text: str) -> Dict[str, int]:
        counts = {}
        for emotion in self.graph.get_emotions():
            for w in self.graph.get_words_for_emotion(emotion):
                hits = kmp_search(w.lower(), text)
                if hits:
                    counts[w.lower()] = counts.get(w.lower(), 0) + len(hits)
        return counts

    def compute_counts(self) -> None:
        self.word_counts = {}
        for song, txt in self.songs.items():
            self.word_counts[song] = self._count_words(txt.lower())


    def optimize(self, max_iters=6000):
        # ensure counts are ready
        if not self.word_counts:
            self.compute_counts()

        # create and store optimizer
        self.optimizer = SimulatedAnnealingOptimizer(
            self.graph,
            self.word_counts,
            self.labels_path
        )

        return self.optimizer.optimize(max_iters=max_iters)

    def score(self, emotion: str) -> List[Tuple[str, float, int]]:
        ranked = []
        for song, counts in self.word_counts.items():
            score = self.graph.score_counts_for_emotion(emotion, counts)
            total = sum(counts.get(w.lower(), 0) for w in self.graph.get_words_for_emotion(emotion))
            ranked.append((song, score, total))
        return sorted(ranked, key=lambda x: x[1], reverse=True)

    def benchmark(self) -> Tuple[float, float]:
        start = time.perf_counter()
        self.compute_counts()
        end = time.perf_counter()
        elapsed = end - start
        throughput = len(self.songs) / elapsed if elapsed > 0 else 0
        return elapsed, throughput
