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

```bash
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

