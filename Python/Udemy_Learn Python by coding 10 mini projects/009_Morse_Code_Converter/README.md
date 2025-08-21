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

## Code `morse_code_converter.py`

```python
#[ Python ]

# class morse converter
class morse_converter:
  
  def __init__(self) -> None:
    self.morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    
    ' ': '/'
    }
  
  # Fungsi ubah ke morse 
  def ubah_ke_morse(self, teks: str) -> str:
    return ' '.join(self.morse_code_dict.get(char.upper(), '') for char in teks)
  
  # Fungsi ubah ke teks 
  def ubah_ke_teks(self, morse: str) -> str:
    list_teks: list[str] = []
    
    for code in morse.split():
      for key, value in self.morse_code_dict.items():
        if value == code:
          list_teks.append(key)
          break
      else:
        list_teks.append('?')
    
    return ''.join(list_teks)
  
  # Fungsi mulai
  def mulai(self) -> None:
    
    print('-'*30)
    print('   [ \033[34mMorse Code Converter\033[0m ]')
    print('-'*30)
    # loop program
    while True:
      
      # input metode handling
      while True:
        self.metode: str = input(
          ' [\033[33ma\033[0m] teks ubah ke morse\n'
          ' [\033[33mb\033[0m] morse ubah ke teks\n'
          ' Pilih Metode [\033[33ma/b\033[0m]: '
          )
        
        if self.metode in ['a', 'A', 'b', 'B', '0']:
          break
        else:
          print('\n\033[31m[ Input Yg Bener ]\033[0m\n')
          print('-'*30)
      
      if self.metode == '0': # stop loop
        print('\n\033[33m[ Program Selesai ]\033[0m\n')
        print('-'*30)
        break
      
      self.user_input: str = input(f'\n > Masukan {"\033[32mteks\033[0m" if self.metode == "a" else "\033[34mmorse\033[0m"}: ')
      self.output: str = self.ubah_ke_morse(self.user_input) if self.metode == 'a' else self.ubah_ke_teks(self.user_input)
      
      print(f'\n > {"\033[34m" if self.metode == "a" else "\033[32m"}{self.output}\033[0m\n')
      print('-'*30)

# main 
def main() -> None:
  app = morse_converter()
  app.mulai()

# run program
if __name__ == '__main__':
  main()

'''
python morse_code_converter.py
'''
```
