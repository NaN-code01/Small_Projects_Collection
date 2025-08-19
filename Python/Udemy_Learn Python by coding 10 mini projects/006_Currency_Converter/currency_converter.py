#[ Python ]

# import modul penting
import json
import requests

# class konversi mata uang 
class Konversi_Mata_Uang:
  
  def __init__(self) -> None:
    
    #---------------------------------------------------------------------------------------
    '''
    [ sumber kurs ]
    LOCAL -> - file bawaan rates.json (kurs tahun 2024)
             - tidak perlu  set base & key
             
    API   -> - requests ke server     (kurs latest)
             - exchangerate-api.com
    
    [ base ]
    LOCAL -> EUR   (otomatis)
    API   -> bebas (IDR, USD EUR, ...)
    
    [ key ]
    - hanya untuk API 
    '''
    # option
    self.sumber_kurs: str = 'LOCAL'
    self.base: str = 'USD'
    self.key: str = '' # api key
    #---------------------------------------------------------------------------------------
    
    self.kurs: dict | None = None
    self.informasi: dict | None = None
    self.pernah_request: bool = False
    
  # Fungsi start
  def start(self) -> None:
    self.kurs: dict = self.ambil_kurs(key=self.key, base=self.base) 
  
  def ambil_kurs(self, key: str, base: str) -> dict:
    # load kurs
    if self.sumber_kurs == 'LOCAL':
      return self.load_kurs('rates.json')
    elif self.pernah_request and self.informasi:
      return self.informasi['conversion_rates']
    elif self.sumber_kurs == 'API':
      if not key:
        raise ValueError('[ API key kosong, tambahkan API key dulu ]')
      self.url: str = f'https://v6.exchangerate-api.com/v6/{key}/latest/{base}'
      self.informasi: dict[str, any] = self.get_info(url=self.url)
      self.pernah_request: bool = True
      return self.informasi['conversion_rates']
  
  # Fungsi get info API 
  def get_info(self, url: str) -> dict | None:
    try:
      response: requests.Response = requests.get(url)
      if response.status_code == 200:
        print(
          '[ Berhasil Terhubung ]\n'
          f' URL    : {url}\n'
          f' Status : {response.status_code}')
        return response.json()
      else:
        print(
          '[ Tidak Bisa Terhubung ]\n'
          f' URL    : {url}\n'
          f' Status : {response.status_code}')
    except Exception as e:
      print(f'[ Error ]\n {e}')
  
  # Fungsi kurs json 
  def load_kurs(self, json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
      return json.load(file)
  
  # Fungsi display kurs yg tersedia di file local json
  def semua_kurs_json(self, kurs_tersedia, kurs: dict[str, dict]) -> str:
    mata_uang: dict = kurs.get(kurs_tersedia)
    kode: str = mata_uang['code'].strip()
    nama: str = mata_uang['name'].strip()
    return f' {kode} : {nama}'
  
  # Fungsi konversi mata uang
  def konversi(self, jumlah: float, kurs_awal: str, kurs_akhir: str, kurs: dict, sumber_kurs: str) -> float:
    
    #---------------------------------------------------------------------------------------
    if sumber_kurs == 'LOCAL':
      
      kurs_awal = kurs_awal.lower()
      kurs_akhir = kurs_akhir.lower()
      
      # cek kurs
      if (kurs_awal in kurs and kurs_akhir in kurs) or (kurs_awal == 'eur' or kurs_akhir == 'eur'):
        
        # return hasil
        if kurs_awal == kurs_akhir:
          return jumlah
        elif kurs_awal == 'eur' or kurs_akhir == 'eur':
          return jumlah * (kurs[kurs_akhir]['rate'] if kurs_awal == 'eur' else kurs[kurs_awal]['inverseRate'])
        else:
          return jumlah * (kurs[kurs_akhir]['rate']/kurs[kurs_awal]['rate'])
      
      # return 0.0 jika kurs tidak ditemukan 
      else:
        print(
          f'[ Kurs: \033[33m{kurs_awal.upper() if kurs_awal not in kurs else kurs_akhir.upper()}\033[0m Tidak Ditemukan ]\n'
          '[ Silahkan Masukan Kurs Yang Tersedia ]\n'
          f'{"-"*55}')
        for kurs_tersedia in kurs:
          print(self.semua_kurs_json(kurs_tersedia=kurs_tersedia, kurs=kurs))
        print('-'*55)
        return 0.0
    #---------------------------------------------------------------------------------------
    elif sumber_kurs == 'API':
      
      kurs_awal = kurs_awal.upper()
      kurs_akhir = kurs_akhir.upper()
      
      # cek kurs
      if kurs_awal not in kurs or kurs_akhir not in kurs:
        print(
          f'[ Kurs : \033[33m{kurs_awal if kurs_awal not in kurs else kurs_akhir}\033[0m Tidak Ditemukan ]\n'
          '[ Silahkan Masukan Kurs Yang Tersedia ]')
        print('-'*7)
        for key in kurs:
          print(f'| {key} |')
        print('-'*7)
        return 0.0
      
      # retun hasil
      else:
        if kurs_awal == kurs_akhir:
          return jumlah
        else:
          return jumlah * (kurs[kurs_akhir]/kurs[kurs_awal])
    #---------------------------------------------------------------------------------------

# main 
def main() -> None:
  app = Konversi_Mata_Uang()
  hasil = app.konversi(
    jumlah=100,
    kurs_awal='usd',
    kurs_akhir='idr',
    kurs=app.ambil_kurs(app.key, app.base),
    sumber_kurs=app.sumber_kurs)
  print(hasil)

# run
if __name__ == '__main__':
  main()

'''
python currency_converter.py
'''