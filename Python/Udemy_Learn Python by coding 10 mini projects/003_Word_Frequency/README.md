# Word Frequency

A Python script to analyze word frequency from user input or from `.txt` and `.pdf` files.

## Features

- Counts word frequency from text input or files.  
- Supports both **manual text input** and **file reading** (`.txt` and `.pdf`).  
- Case-insensitive analysis (ignores uppercase/lowercase).  
- Dynamically aligns output based on the longest word length.  
- Safely manages invalid or unexpected input (wrong menu choice, missing files, etc.).

## Notes

- ‼️This code is mostly written in Indonesian (function names, variables, prompts, and comments). Non-Indonesian speakers might need additional effort to read or modify the code.  
- `.pdf` reading requires the `pypdf` library. If not installed, `.pdf` files cannot be processed.  
- `.txt` files must be UTF-8 encoded for proper reading.  

## Requirements

- Python 3.x  
- Library:  
  - `pypdf` (for `.pdf` support)  

---

## Usage

1. Run the script in your terminal:

```bash
python word_frequency.py
```

2. Choose input method:
   - **[1] Manual Text Input** → Type/paste a paragraph.
   - **[2] File Input** → Provide the path to a `.txt` or `.pdf` file.

3. The program will process and display:
   - List of words
   - Frequency of each word
   - Aligned output for readability

---

## Example Output

### [1] Manual Input

```bash
--------------------------------------------------
      ===[ [ [ [  Frekuensi Kata  ] ] ] ]===
--------------------------------------------------
 [1] Ketik teks manual  (maks 1 paragraf)
 [2] Baca file          (butuh directory)
Tentukan Metode Input [1/2]: 1
--------------------------------------------------
Masukan Teks: Hello world hello Python Python Python
--------------------------------------------------
hello   : 2
world   : 1
python  : 3
--------------------------------------------------
```

### [2] File Input (`sample.txt`)

```bash
--------------------------------------------------
      ===[ [ [ [  Frekuensi Kata  ] ] ] ]===
--------------------------------------------------
 [1] Ketik teks manual  (maks 1 paragraf)
 [2] Baca file          (butuh directory)
Tentukan Metode Input [1/2]: 2
--------------------------------------------------
Bisa membaca file: .txt
                   .pdf
Tuliskan [nama file / directory]:
sample.txt
--------------------------------------------------
this    : 2
is      : 1
a       : 1
sample  : 2
text    : 1
file    : 1
--------------------------------------------------
```

---

## Error Handling

The program includes several checks to prevent crashes and guide the user:

1. **Invalid menu input**  
   - If the user enters something other than `1` or `2` at the input method prompt:  
     ```
     [ Input Yg Bener ]
     ```

2. **File not found or unreadable**  
   - If the specified `.txt` or `.pdf` file does not exist or cannot be opened:  
     ```
     [ Error ]
     ```
   - This also applies to corrupted files or unsupported content.

3. **Unsupported file type**  
   - Only `.txt` and `.pdf` files are supported.  
   - Any other file type is rejected safely with `[ Error ]`.

4. **Unreadable PDF content**  
   - If a `.pdf` file cannot be read by `pypdf` (missing library, encrypted file, or corrupted file), the program catches the exception and prints `[ Error ]`.

5. **General exceptions**  
   - Any unexpected errors during file reading or input handling are caught and displayed, preventing program crashes.

---

## Code ``

```python

```
