# # Count 'um' Script

## Overview
This Python script counts occurrences of the word "um" in a given text input. It ensures that "um" is counted only as a standalone word, regardless of capitalization.

## Requirements
- Python 3

## Usage
1. Run the script:
   python script.py
2. Enter a text input when prompted.
3. The script will output the number of times "um" appears as a standalone word.

## Code Explanation
- `import re`: Imports the regular expressions module to facilitate pattern matching.
- `import sys`: (Not used in the script, but typically included for command-line arguments or input handling.)
- `count(s)`: Uses `re.findall(r"\bum\b", s, re.IGNORECASE)` to find standalone instances of "um".
- `main()`: Prompts the user for input and prints the count of "um" occurrences.
- The script executes `main()` when run directly.

## Example
$ python script.py
Text: Um, excuse me, but um... are you sure?
2

## Notes
- The `\b` ensures that only standalone instances of "um" are counted, avoiding substrings like "umbrella".
- Case insensitivity (`re.IGNORECASE`) allows detection of variations like "Um" and "UM".

## License
This script is open-source and free to use or modify.
