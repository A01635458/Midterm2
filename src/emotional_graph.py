#emotional_graph.py
#guarda palabras de emociones con peso

import json
import os
from typing import Dict, List


class EmotionalGraph:
    def __init__(self, emotions_path: str) -> None:
        if not os.path.exists(emotions_path):
            raise FileNotFoundError(f"{emotions_path} not found")

        with open(emotions_path, "r", encoding="utf-8") as f:
            self.emotion_to_words: Dict[str, List[str]] = json.load(f)

        self.weights: Dict[str, Dict[str, float]] = {}
        self._init_weights()

    def _init_weights(self) -> None:
        for emotion, words in self.emotion_to_words.items():
            self.weights[emotion] = {w.lower(): 1.0 for w in words}

    def get_emotions(self) -> List[str]:
        return list(self.emotion_to_words.keys())

    def get_words_for_emotion(self, emotion: str) -> List[str]:
        return self.emotion_to_words.get(emotion, [])

    def get_weight(self, emotion: str, word: str) -> float:
        return self.weights.get(emotion, {}).get(word.lower(), 0.0)

    def set_weight(self, emotion: str, word: str, val: float) -> None:
        self.weights[emotion][word.lower()] = max(0.0, val)

    def score_counts_for_emotion(self, emotion: str, counts: Dict[str, int]) -> float:
        score = 0.0
        for w, c in counts.items():
            score += self.get_weight(emotion, w) * c
        return score

    def score_counts_all(self, counts: Dict[str, int]) -> Dict[str, float]:
        return {e: self.score_counts_for_emotion(e, counts) for e in self.get_emotions()}
