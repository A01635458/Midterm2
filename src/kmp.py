# kmp.py
# Simple KMP implementation for pattern searching.

from typing import List


def build_lps(pattern: str) -> List[int]:
    """
    Build Longest Prefix Suffix (LPS) array for KMP.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(pattern: str, text: str) -> List[int]:
    """
    Return all starting positions where pattern appears in text.
    """
    if not pattern or not text:
        return []

    pattern = pattern.lower()
    text = text.lower()

    lps = build_lps(pattern)
    matches = []

    i = 0  # text index
    j = 0  # pattern index

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches
