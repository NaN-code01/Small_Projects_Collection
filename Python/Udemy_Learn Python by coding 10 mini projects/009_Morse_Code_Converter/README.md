# Morse Code Converter

A Python script to **convert text into Morse code** and **Morse code back into text** with a simple interactive terminal interface.

## Features

- Convert **text → Morse code**.
- Convert **Morse code → text**.
- Supports **letters (A–Z)**, **numbers (0–9)**, **punctuation** (.,?! etc.), and spaces.
- Handles invalid/unknown Morse codes by replacing them with `?`.
- Interactive menu with colored terminal output.
- Option to **exit the program** anytime.

## Notes

- ‼️This script is mostly written in Indonesian (variable names, prompts, and comments).  
- Uses ANSI escape codes (`\033`) for terminal color formatting. On some terminals, colors may not display.  
- Unknown characters that are not in the Morse dictionary will be ignored (for text input) or replaced with `?` (for Morse input).  

## Requirements

- Python 3.x

---

## Usage

1. Run the script in your terminal:

```bash
python morse_code_converter.py
```

2. You will see the main menu:

```bash
------------------------------
   [ Morse Code Converter ]
------------------------------
 [a] teks ubah ke morse
 [b] morse ubah ke teks
 Pilih Metode [a/b]:
```

3. Choose an option:

   `[a]` → Convert text to Morse.
   `[b]` → Convert Morse to text.
   `[0]` → Exit the program.

4. Input your text or Morse code:

   - For text to Morse: type normal text (e.g., `HELLO`).
   - For Morse to text: type Morse codes separated by spaces (e.g., `.... . .-.. .-.. ---`).

5. The program will display the converted result with colored output.

---

## Example Output

- **Text → Morse `[a]`**

```bash
------------------------------
 [a] teks ubah ke morse
 [b] morse ubah ke teks
 Pilih Metode [a/b]: a

 > Masukan teks: SOS

 > ... --- ...
------------------------------
```

- **Morse → Text `[b]`**

```bash
------------------------------
 [a] teks ubah ke morse
 [b] morse ubah ke teks
 Pilih Metode [a/b]: b

 > Masukan morse: .... . .-.. .-.. ---

 > HELLO
------------------------------
```

- **Exit `[0]`**

```bash
[ Program Selesai ]
------------------------------
```

---

## Error Handling

The program includes some simple error messages:

- Invalid menu input

  ```bash
  [ Input Yg Bener ]
  ```
  → Shown if you enter something other than a, b, or 0.

- Unknown Morse code
  Example: if you type `---..-` which is not in the dictionary, it will show:
  ```bash
  HEL?O
  ```
  → Invalid Morse sequences are replaced with ?.

---

## Code ``

```python

```
