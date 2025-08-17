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

## Code `word_frequency.py`

```python
#[ Python ]

# import fungsi penting
import time as t
from collections import Counter
import re
import os

# import fungsi pdf reader (kalo punya)
try:
  from pypdf import PdfReader
except Exception:
  None

# fungsi menentukan frekuensi
def tentukan_frekuensi(teks: str) -> list[tuple[str, int]]:
  teks_kecil: str = teks.lower() # jadi tidak bisa membedakan huruf besar/kecil
  global list_kata
  list_kata = re.findall(r'\b\w+\b', teks_kecil)
  hitung_kata: Counter = Counter(list_kata)
  return hitung_kata.most_common()

# fungsi mencari kata terpanjang
def kata_terpanjang(list_kata: list[str]) -> int:
  return max((len(kata) for kata in list_kata), default=0)

# fungsi hollow (rapihin spasi)
def hollow(key, panjang: int) -> str:
  return ' ' * (panjang - len(str(key)))

# fungsi mengecek file .pdf
def apakah_pdf(filepath):
    return os.path.isfile(filepath) and filepath.lower().endswith(".pdf")

# fungsi baca file .pdf .txt
def baca(file: str) -> str:
  if apakah_pdf(file): # untuk .pdf
    pembaca_pdf = PdfReader(file)
    semua_teks = ""
    for halaman in pembaca_pdf.pages:
      teks = halaman.extract_text()
      if teks:
        semua_teks += teks + "\n"
    return str(semua_teks)
  else: # untuk .txt
    with open(file, encoding='utf-8', errors='ignore') as f:
      return str(f.read())

# main
def main() -> None:
  print(f'{"-"*50}\n'
  '      ===[ [ [ [  Frekuensi Kata  ] ] ] ]===      ')
  # handle input teks str
  while True:
    print('-'*50)
    metode_input = input(
      ' [1] Ketik teks manual  (maks 1 paragraf)\n'
      ' [2] Baca file          (butuh directory)\n'
      'Tentukan Metode Input [1/2]: '
      )
    try:
      if metode_input == '1':
        print('-'*50)
        teks: str = str(input('Masukan Teks:\n'))
        break
      elif metode_input == '2':
        print('-'*50)
        directory: str = str(input(
          'Bisa membaca file: .txt\n'
          '                   .pdf\n'
          'Tuliskan [nama file / directory]:\n'))
        teks: str = baca(directory)
        break
      else:
        print('\n[ Input Yg Bener ]\n')
    except Exception as e:
      print(f'\n[ Error ]\n{e}')
  
  # hitung frekuensi kata
  frekuensi_kata: list[tuple[str, int]] = tentukan_frekuensi(teks)
  
  # display hasil
  t.sleep(1.5)
  print('-'*50)
  for kata, frekuensi in frekuensi_kata:
    print(f'{kata}{hollow(kata, kata_terpanjang(list_kata))} : {frekuensi}')
  print('-'*50)

# jalanin kode
if __name__ == '__main__':
  main()

'''
python word_frequency.py
'''
```
