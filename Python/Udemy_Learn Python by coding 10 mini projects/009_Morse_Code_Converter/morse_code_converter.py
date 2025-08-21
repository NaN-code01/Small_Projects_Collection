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