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