# Text Analyzer

A Python script to analyze a text file by counting characters, words, spaces, and showing the most frequently used words.

## Features

- Reads text directly from a file.
- Calculates:
  - Total characters (with and without spaces).
  - Total spaces.
  - Total words.
- Displays the **top N most frequent words** (default: 10).
- Output is formatted neatly with highlights for easier readability.

## Notes

- ‼️This code is mostly written in Indonesian (variable names, prompts, and comments). Users who are not familiar with the Indonesian language may find it harder to read or modify.
- Default file to analyze: `note.txt`.  
  (Change this in the `main()` function if you want to analyze another file.)
  ```python
  def main() -> None:
  teks_file: str = 'note.txt' #directory
  ```
- Regular expressions (`re`) are used to detect words more accurately than simple split.

## Requirements

- Python 3.x
- Standard Library modules:  
  - `collections`  
  - `re`

---

## Usage

1. Prepare a text file, e.g., `note.txt`, in the same directory as the script.

2. Run the script in your terminal:

```bash
python text_analyzer.py
```

3. The program will output analysis results, including:
   - Total characters (with and without spaces).
   - Total spaces.
   - Total words.
   - A list of the most frequent words and their counts.

---

## Example Output

```bash
----------------------------------------
           [ Text Analyzer ]
----------------------------------------
 Total karakter (termasuk spasi) : 3921
 Total karakter (tanpa spasi)    : 3314
 Total spasi                     : 607
 Total kata                      : 630
 Kata yang sering muncul         : 
  > the        : 47
  > and        : 19
  > to         : 19
  . . .
----------------------------------------
```

---

## Error Handling

The program handles several scenarios:

- **File not found**  
  Occurs if the target file (default: `note.txt`) does not exist in the directory.  
  A Python `FileNotFoundError` will be raised.

- **Empty file**  
  If the file exists but is empty, all analysis results will be `0`.

---

## Code ``

```python

```
