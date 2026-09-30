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

    def process_file(self):
        """Count every word in the file. Return True on success, False if the file is missing."""
        extra_punctuation = "“”‘’—–"
        translator = str.maketrans("", "", string.punctuation + extra_punctuation)

        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            print(f"\nProcessing '{self.__filepath.name}'...\n")
            with self.__filepath.open("r", encoding="utf-8-sig") as file:
                for line in file:
                    line = line.translate(translator).lower()
                    for word in line.split():
                        if word in self.__stop_words:
                            continue
                        self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            return True

        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath.name}' was not found.")
            return False

    def print_report(self):
        """Print each word and its count in alphabetical order."""
        words = sorted(self.__frequencies.keys())
        if not words:
            print("No words found.")
            return

        width = max(len(word) for word in words)
        for word in words:
            print(f"{word:<{width}} :: {self.__frequencies[word]}")

def main():
    """Display the file menu and run the analyzer on the user's choice."""
    text_folder = Path(__file__).parent / "text_files"
    files = {
        "1": text_folder / "monte_cristo.txt",
        "2": text_folder / "princess_mars.txt",
        "3": text_folder / "tarzan.txt",
        "4": text_folder / "treasure_island.txt",
    }
    exit_choice = str(len(files) + 1)

    stop_words = ["the", "a", "an", "and", "or", "of", "to", "in", "is", "it"]

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key, path in files.items():
            print(f"{key}. {path.stem.replace('_', ' ').title()}")
        print(f"{exit_choice}. Exit")

        choice = input(f"\nEnter your choice (1-{exit_choice}): ").strip()

        if choice == exit_choice:
            print("\nGoodbye!")
            break

        if choice in files:
            analyzer = WordAnalyzer(files[choice], stop_words)
            if analyzer.process_file():
                analyzer.print_report()
        else:
            print(f"\nInvalid choice. Please select from 1-{exit_choice}.")

        input("\nPress Enter to return to the menu... ")


if __name__ == "__main__":
    main()
