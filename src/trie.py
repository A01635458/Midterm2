# trie.py
# Simple Trie to store lyric words.

from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_word(self, word: str) -> None:
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def insert_text(self, text: str) -> None:
        for raw_word in text.split():
            word = "".join(c for c in raw_word if c.isalpha())
            if word:
                self.insert_word(word)

    def contains(self, word: str) -> bool:
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
