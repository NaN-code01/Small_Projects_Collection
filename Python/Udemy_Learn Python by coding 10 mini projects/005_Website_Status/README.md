# Website Status Checker

A simple **Python script** that checks the status of a website.  
It fetches the response using the `requests` library, extracts important metadata, and converts the server timestamp into **Indonesian Local Time (WIB)**.

## Features

- Check a website's status using HTTP GET request.  
- Display detailed response information:
  - URL  
  - Status Code  
  - Content Type  
  - Content Length  
  - Server  
  - Date (converted to WIB with Indonesian format)  
  - Response Time (seconds)  
- Custom date formatter with **Indonesian day and month names**.  
- Includes simple error handling (e.g., connection issues).  

## Notes

- ‼️This code is mostly written in **Indonesian** (function names, variables, prompts, and comments). Non-Indonesian speakers might need additional effort to read or modify the code.  
- Only works on websites that are accessible over the internet.  
- Suitable for small website status checks, not a full monitoring tool.  

## Requirements

- Python 3.x  
- [Requests](https://pypi.org/project/requests/) library  

Install the dependency:

```bash
pip install requests
```

---

## Usage
1. Run the script in your terminal:

```bash
python website_status.py
```

2. The script automatically checks the status of the URL set in `url_yg_dicek` (default: `https://www.wikipedia.org/`).

3. You can modify the URL by editing this line in the code:

```python
url_yg_dicek: str = 'https://www.wikipedia.org/'
```

4. After running, the program will display website information and status in the terminal.

---

## Example Output

```
=======================================================
               [ WEBSITE STATUS CHECKER ]
=======================================================
-------------------------------------------------------
 URL            : https://www.wikipedia.org/
 Status Code    : 200
 Tipe Konten    : text/html; charset=UTF-8
 Panjang Konten : 64823 byte
 Server         : mw1363.eqiad.wmnet
 Tanggal        : Senin, 19 Agustus 2025 11:25:32
 Waktu Respon   : 0.32 detik
-------------------------------------------------------
```

If an error occurs (e.g., URL not reachable):

```
[ Error ]: HTTPSConnectionPool(host='example.com', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x...>: Failed to establish a new connection'))
```

---

## Code `website_status.py`

```python
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
```
