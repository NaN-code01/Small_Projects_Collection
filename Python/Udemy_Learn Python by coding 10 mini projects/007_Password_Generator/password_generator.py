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