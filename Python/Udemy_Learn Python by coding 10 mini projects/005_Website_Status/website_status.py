#[ Python ]

# Import modul penting
import requests as rqs
from datetime import datetime, timedelta # dt:1 = modul, dt:2 = class dlm modul

# Fungsi pengatur tanggal ke tanggal waktu indo (WIB)
def pengatur_tanggal(tanggal_awal: str) -> str:
  try:
    tanggal_wib = datetime.strptime(tanggal_awal, '%a, %d %b %Y %H:%M:%S GMT') + timedelta(hours=7)
    
    # tupple hari & bulan 
    nama_hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')
    nama_bulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
              'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
    
    # format ke indo
    hari = nama_hari[tanggal_wib.weekday()]
    bulan = nama_bulan[tanggal_wib.month - 1]
    tanggal_terformat: str = f'{hari}, {tanggal_wib.day} {bulan} {tanggal_wib.year} {tanggal_wib.strftime("%H:%M:%S")}'
    
    # return tanggal
    return tanggal_terformat
    
  except Exception:
    return '- - - -'

# Fungsi pengecekan status url
def cek_status(url: str) -> None:
  try:
    respon: rqs.Response = rqs.get(url)
    
    # ngambil informasi dari respon 
    headers        : rqs.structures.CaseInsensitiveDict[str] = respon.headers
    status_code    : int = respon.status_code
    tipe_konten    : str = headers.get('Content-Type', 'Unknown')
    panjang_konten : str = f"{headers.get('Content-Length') or len(respon.content)} byte"
    server         : str = headers.get('Server', 'Unknown')
    tanggal        : str = pengatur_tanggal(headers.get('Date', 'Unknown'))
    waktu_respon   : float = respon.elapsed.total_seconds()
    
    # display informasi terkait url
    print(
      f'={"-"*53}=\n'
      f'{" "*((55-26)//2)}\033[1;94m[ WEBSITE STATUS CHECKER ]\033[0m\n'
      f'={"-"*53}=\n'
      )
    print('-'*55)
    print(f' URL            : \033[36m{url}\033[0m')
    print(f' Status Code    : \033[34m{status_code}\033[0m')
    print(f' Tipe Konten    : \033[36m{tipe_konten}\033[0m')
    print(f' Panjang Konten : \033[34m{panjang_konten}\033[0m')
    print(f' Server         : \033[36m{server}\033[0m')
    print(f' Tanggal        : \033[34m{tanggal}\033[0m')
    print(f' Waktu Respon   : \033[36m{waktu_respon:.2f} detik\033[0m')
    print('-'*55)
  except rqs.RequestException as e:
    print(f'\n[ Error ]: \033[34m{e}\033[0m')

# main 
def main() -> None:
  url_yg_dicek: str = 'https://www.wikipedia.org/'
  cek_status(url_yg_dicek)

# run program
if __name__ == '__main__':
  main()

'''
python website_status.py
'''