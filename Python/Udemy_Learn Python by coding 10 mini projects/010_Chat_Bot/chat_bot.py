#[ Python ]

# import modul
from difflib import SequenceMatcher
from datetime import datetime
import requests
import time

# class chatbot
class ChatBot:
  
  def __init__(self, nama: str, respon: dict[str, str]) -> None:
    self.nama = nama
    self.respon = respon
    
    # API BMKG (cuaca)
    self.pernah_APIcuaca: bool = False
    self.adm4_code: str = '36.73.01.1001'  # Kecamatan Serang, Kota Serang
    self.url_BMKG: str = f'https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={self.adm4_code}'
  
  # Fungsi request API 
  @staticmethod
  def req(url: str) -> dict | None:
    try:
      response = requests.get(url)
      if response.status_code == 200:
        return response.json()
      else:
        print(f' [ ada yg ga beres... Status Code: ({response.status_code}) ]')
    except Exception as e:
      print(f' [ ERROR ]\n{e}')
    
  # Fungsi kalkulasi kemiripan urutan antara input dan respon 
  @staticmethod
  def kalkulasi(kalimat_input: str, kalimat_respon: str) -> float:
    urutan: SequenceMatcher = SequenceMatcher(a=kalimat_input, b=kalimat_respon)
    return urutan.ratio()
  
  # Fungsi ambil respon terbaik (tercocok)
  def respon_terbaik(self, user_input: str) -> tuple[str, float]:
    self.kemiripan_tertinggi: float = 0.0
    self.respon_cocok: str = 'Ga paham, coba ketik yg lain' # respon kalo ga ada input yg cocok
    
    # cek
    for respon in self.respon:
      self.kemiripan: float = self.kalkulasi(user_input, respon) 
      
      if self.kemiripan > self.kemiripan_tertinggi:
        self.kemiripan_tertinggi = self.kemiripan
        if self.kemiripan >= 0.5:
          self.respon_cocok = self.respon[respon]
    
    return self.respon_cocok, self.kemiripan_tertinggi
  
  # Fungsi mulai
  def mulai(self) -> None:
    print(
      f'{"-"*40}\n'
      f'{" "*14}[ \033[34mChat Bot\033[0m ]\n'
      f'{"-"*40}\n'
      )
    time.sleep(0.5)
    
    print(f'Halo... Namaku \033[34m{self.nama}\033[0m, mo ngapain?\n')
    time.sleep(0.5)
    
    while True:
      self.user_input: str = input('Input: ')
      print('-'*5)
      self.respon_bot, self.kecocokan = self.respon_terbaik(self.user_input)
      time.sleep(0.5)
      
      # respon waktu
      if self.respon_bot == 'GET_TIME':
        self.respon_bot = f'Jam sekarang: {datetime.now():%H:%M}'
      
      # respon cuaca
      if self.respon_bot == 'GET_CUACA':
        
        if self.pernah_APIcuaca:
          self.respon_bot = str(
            f'\n{"-"*30}\n'
            f'Lokasi : {self.display_lokasi}\n'
            f'{"-"*30}\n'
            f'{self.display_cuaca if self.cuaca else "Data prakiraan tidak ditemukan."}\n'
            f'{"-"*30}'
            )
        
        else:
          self.data_cuaca = self.req(url=self.url_BMKG)
          if self.data_cuaca:
            
            self.lokasi = self.data_cuaca.get('lokasi', {})
            self.display_lokasi = f'Kecamatan {self.lokasi.get("kecamatan", "")}, {self.lokasi.get("kotkab", "")}, {self.lokasi.get("provinsi", "")}'
            
            self.cuaca_list = self.data_cuaca.get('data', [])
            self.cuaca = self.cuaca_list[0].get('cuaca', [])
            
            self.display_cuaca = str(
              f'Cuaca            : {self.cuaca[0][0].get("weather_desc")}\n'
              f'Suhu Udara       : {self.cuaca[0][0].get("t")}℃\n'
              f'Kelembapan Udara : {self.cuaca[0][0].get("hu")}%\n'
              f'Tutupan Awan     : {self.cuaca[0][0].get("tcc")}%\n'
              f'Curah Hujan      : {self.cuaca[0][0].get("tp")} mm\n'
              f'Kecepatan Angin  : {self.cuaca[0][0].get("ws")} Km/jam\n'
              f'Waktu Perkiraan  : {self.cuaca[0][0].get("local_datetime")}\n'
              f'Update Terakhir  : {self.cuaca[0][0].get("utc_datetime")}'
              )
            
            self.respon_bot = str(
              f'\n{"-"*30}\n'
              f'Lokasi : {self.display_lokasi}\n'
              f'{"-"*30}\n'
              f'{self.display_cuaca if self.cuaca else "Data prakiraan tidak ditemukan."}\n'
              f'{"-"*30}'
              )
            self.pernah_APIcuaca = True
      
      # output respon
      print(f'\033[34m{self.nama}: {self.respon_bot} \033[30m({self.kecocokan:.2%})\033[0m\n')
      
      if self.respon_bot in ['Sampai jumpa lagi.', 'Sampai jumpa.']:
        print('[ Program Selesai ]')
        break

# main 
def main() -> None:
  respon: dict[str, str] = {
    'halo': 'Hai!',
    'apa kabar': 'Baik, terima kasih. Kamu?',
    'siapa kamu': 'Aku adalah program sederhana untuk menjawab pertanyaanmu.',
    'makasih': 'Sama-sama.',
    'selamat tinggal': 'Sampai jumpa lagi.',
    'dadah': 'Sampai jumpa.',
    'kamu ngantuk?': 'Tidak, masih siap membantu.',
    'lapar': 'Mungkin waktunya makan.',
    'kenapa langit biru?': 'Karena cahaya biru tersebar lebih banyak oleh atmosfer.',
    'lagi apa': 'Sedang menunggu perintah berikutnya.',
    'kamu manusia?': 'Bukan, aku hanya sebuah program.',
    'jam berapa?': 'GET_TIME',
    'cuaca sekarang?': 'GET_CUACA'
    }
    
  chatbot = ChatBot(nama='Bot', respon=respon)
  chatbot.mulai()

# run program
if __name__ == '__main__':
  main()

'''
python chat_bot.py
'''