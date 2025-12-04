# tests/test_kmp.py
# Basic functionality tests for the KMP implementation.

import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.append(SRC)

from kmp import kmp_search


def test_kmp_basic():
    text = "abababa"
    pattern = "aba"
    result = kmp_search(pattern, text)
    assert result == [0, 2, 4], f"Expected [0,2,4], got {result}"
    print("✔ KMP basic test passed.")


def test_kmp_no_match():
    text = "hello world"
    pattern = "xyz"
    result = kmp_search(pattern, text)
    assert result == [], f"Expected [], got {result}"
    print("✔ KMP no-match test passed.")


def test_kmp_single_match():
    text = "this is a test"
    pattern = "test"
    result = kmp_search(pattern, text)
    assert result == [10], f"Expected [10], got {result}"
    print("✔ KMP single match test passed.")


if __name__ == "__main__":
    test_kmp_basic()
    test_kmp_no_match()
    test_kmp_single_match()
    print("ALL KMP TESTS PASSED")
