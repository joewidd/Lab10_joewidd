"""
Text Analyzer,
Joe Widdifield,
Create text analyzer that counts how many words are in a specified file,
9/29/2026
"""
from pathlib import Path
import string


class WordAnalyzer:
    """Reads a text file and counts how often each word appears."""

    def __init__(self, filepath, stop_words=None):
        """Store the file path as a Path object and set up an empty frequency dictionary."""
        self.__filepath = Path(filepath)
        self.__frequencies = {}
        self.__stop_words = set(word.lower() for word in stop_words) if stop_words else set()

