import re
import sys

def main():
    print(count(input("Text: ")))  # Get user input and print the count of "um"

def count(s):
    """
    Counts occurrences of the word "um" (case-insensitive) as a standalone word.
    """
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)  # \b ensures "um" is a standalone word
    return len(matches)  # Return the count of matches

if __name__ == "__main__":
    main()
