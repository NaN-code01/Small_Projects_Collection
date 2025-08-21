#[ Python ]

# import modul
from collections import Counter
import re

# class analisis teks 
class analisis_teks:
  
  def __init__(self, directory: str) -> None:
    self.directory: str = directory
    self.teks: str = self.buka_file(self.directory)

  # Fungsi buka file 
  def buka_file(self, path: str) -> str:
    with open(path, 'r') as file:
      teks: str = file.read()
      return teks
  
  # Fungsi menghitung frekuensi kata
  def frekuensi(self, teks: str, banyak_kata: int = 5) -> dict[str, int]:
    teks_kecil: str = teks.lower()
    
    list_kata: list = re.findall(r'\b\w+\b', teks_kecil)
    list_frekuensi: list[tuple[str, int]] = Counter(list_kata).most_common(banyak_kata)
    
    dict_frekuensi: dict[str, int] = {}
    for urutan in list_frekuensi:
      kata: str = urutan[0]
      frekuensi: int = urutan[1]
      dict_frekuensi[kata] = frekuensi
    
    return dict_frekuensi
  
  # Fungsi analisis teks
  def analisis(self, teks: str) -> dict[str, int | dict[str, int]]:
    hasil: dict = {
      'total_karakter_(termasuk_spasi)': len(teks),
      'total_karakter_(tanpa_spasi)': len(teks.replace(' ', '')),
      'total_spasi': teks.count(' '),
      'total_kata': len(teks.split()),
      'kata_yang_sering_muncul': self.frekuensi(teks, 10)
    }
    return hasil
  
  # Fungsi mulai
  def mulai(self) -> None:
    self.hasil_analisis: dict[str, int] = self.analisis(teks=self.teks)
    
    print('-'*40)
    print(f'{" "*11}[ \033[34mText Analyzer\033[0m ]')
    print('-'*40)
    for key, value in self.hasil_analisis.items():
      print(f' {key.replace("_", " ").capitalize():<31} : ', end='')
      
      if isinstance(value, int):
        print(value)
      elif isinstance(value, dict):
        print()
        for kata, frekuensi in value.items():
          print(f'  > \033[33m{kata:<10}\033[0m : {frekuensi}')
    print('-'*40)

# main 
def main() -> None:
  teks_file: str = 'note.txt' #directory
  
  app = analisis_teks(teks_file)
  app.mulai()

# run program
if __name__ == '__main__':
  main()

'''
python text_analyzer.py
'''