# Password Generator

A Python script for generating secure passwords with customizable options.

## Features

- Generate random passwords with **letters, numbers, uppercase letters, and symbols**.  
- Configurable password **length**.  
- Option to include **uppercase letters**.  
- Option to include **symbols**.  
- Check password **strength** automatically:
  - Strong → ≥16 characters, includes uppercase letters and symbols.
  - Weak → does not meet the above criteria.  
- Display **10 passwords** at once in alternating colors in the console.

## Notes

- ‼️The script is written mostly in Indonesian (variable names, comments, and messages).  
- **Strong password** requires:
  - At least 16 characters
  - At least one uppercase letter
  - At least one symbol  
- The script uses ANSI escape codes to color the console output.  
- You can generate passwords of **different lengths** or toggle **uppercase/symbols** by editing the `Password` class parameters.

## Requirements

- Python 3.x  

No external libraries required (uses standard `secrets` and `string` modules).

---

## Usage

1. **Prepare the script**  
   Save the file as `password_generator.py`.

2. **Edit options** (optional)  
   Inside the `main` function:
   ```python
   pw: Password = Password(
       panjang=16,       # length of password
       huruf_besar=True, # include uppercase letters
       simbol=True       # include symbols
       )
   ```

3. **Run the script**
   ```bash
   python password_generator.py
   ```

---

## Example Output

```
--------------------------------------
        [ PASSWORD GENERATOR ]
--------------------------------------
  q2!kL7x@9m#fH4a& | Password Kuat
  4p$rG8vYw1b*Q3c! | Password Kuat
  m9#hU7e@2nL0t^5z | Password Kuat
  ...
--------------------------------------
```

- Strong passwords are highlighted in blue (`Password Kuat`).
- Weak passwords are highlighted in red (`Password Lemah`).

---

## Code `password_generator.py`

```python
#[ Python ]

# imporn modul
import secrets
import string

# Class Password 
class Password:
  
  def __init__(self, panjang: int = 12, huruf_besar: bool = True, simbol: bool = True) -> None:
    self.panjang = panjang
    self.pake_huruf_besar = huruf_besar
    self.pake_simbol = simbol
    
    self.base_char: str = string.ascii_lowercase + string.digits
    
    if self.pake_huruf_besar:
      self.base_char += string.ascii_uppercase
    if self.pake_simbol:
      self.base_char += string.punctuation
  
  # Fungsi buat bikin password
  def buat(self) -> str:
    password: list[str] = []
    
    for char in range(self.panjang):
      password.append(secrets.choice(self.base_char))
    
    return ''.join(password)
  
  # Fungsi cek kekuatan(keamanan) password 
  def cek(self, password: str) -> bool:
    if len(password) >= 16 and any(char in string.ascii_uppercase for char in password) and any(char in string.punctuation for char in password):
      return True
    else:
      return False

# main 
def main() -> None:
  pw: Password = Password(
    panjang=16,
    huruf_besar=True,
    simbol=True
    )
  warna = ['\033[37m', '\033[30;47m']
  # display
  print('-'*38)
  print(f'{" "*8}[ \033[34mPASSWORD GENERATOR\033[0m ]')
  print('-'*38)
  for i in range(10):
    password = pw.buat()
    apa_kuat = pw.cek(password=password)
    print(f' {warna[i % len(warna)]} {password} \033[0m | {"\033[34mPassword Kuat\033[0m" if apa_kuat else "\033[31mPassoword Lemah\033[0m"}')
  print('-'*38)

# run code
if __name__ == '__main__':
  main()

'''
python password_generator.py
'''
```
