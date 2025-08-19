# Currency Converter

A Python script for converting currencies using either a **local JSON file** (offline rates) or **real-time exchange rates** via the [Exchangerate API](https://www.exchangerate-api.com/).

## Features

- Convert between multiple currencies.  
- Works with **two data sources**:  
  - **LOCAL** → Offline JSON file (`rates.json`) with 2024 currency rates.  
  - **API** → Live exchange rates from `exchangerate-api.com`.  
- Supports **base currency configuration**.  
- Detects and handles unavailable currencies.  
- Provides clear error messages for invalid or missing inputs.  
- Automatically prints available currencies when an invalid one is entered.

## Notes

- ‼️The script is written mostly in Indonesian (variable names, comments, and messages).  
- **LOCAL mode** always uses **EUR** as the base currency.  
- **API mode** allows any base currency (USD, IDR, EUR, etc.).  
- When using **API mode**, you need to add your own **API key** in `self.key`.  
- If the source and target currencies are the same, the original amount is returned.  
- Missing currencies return `0.0` and display the available options.

## Requirements

- Python 3.x  
- `requests` library  

Install dependencies:  

```bash
pip install requests
```

---

## Usage

1. **Prepare the script**  
   Save the file as `currency_converter.py`.
   ```python
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
   ```

3. **Choose data source**  
   In the class `Konversi_Mata_Uang` (inside the code), set:
   ```python
     # option
     self.sumber_kurs: str = 'LOCAL'
   ``` 
   - `self.sumber_kurs = 'LOCAL'` → use `rates.json` (offline).  
   - `self.sumber_kurs = 'API'` → use live rates (requires API key).  

4. **If using LOCAL mode**  
   - Make sure you have `rates.json` in the same folder.  
   - Example structure:
     ```json
     ...
     "usd": {
       "code": "USD",
       "alphaCode": "USD",
       "numericCode": "840",
       "name": "U.S. Dollar",
       "rate": 1.0881034985423,
       "date": "Sat, 20 Jul 2024 00:55:11 GMT",
       "inverseRate": 0.91903022216148
     },
     ...
     ```

5. **If using API mode**  
   - Sign up at [Exchangerate API](https://www.exchangerate-api.com/) to get a free API key.  
   - Set your API key inside the class:  
     ```python
     # option
     ...
     self.key: str = '' # api key
     ```

6. **Edit the script**
   - Edit the parameters in `hasil = app.konversi(...)` variable on the `main` function:
     - `jumlah` -> amount of money to convert
     - `kurs_awal` -> source currency code (e.g. "usd")
     - `kurs_akhir` -> target currency code (e.g. "idr")
     ```python
     ...
     hasil = app.konversi(
     jumlah=100,
     kurs_awal='usd',
     kurs_akhir='idr',
     kurs=app.ambil_kurs(app.key, app.base),
     sumber_kurs=app.sumber_kurs)
     ...
     ```
   
8. **Run the script**  
   ```bash
   python currency_converter.py
   ```

---

## Example Output  

### Using **LOCAL** source  
```bash
1630000.0
```

### Using **API** source  
```bash
[ Connected Successfully ]
 URL    : https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD
 Status : 200
1625000.0
```

---

## Error Handling

This program already includes several error handling mechanisms:

1. **Empty API Key**  
   - If the source is set to `API` but the key is not provided, the program will show:  
     ```
     [ API key kosong, tambahkan API key dulu ]
     ```

2. **Failed to connect to API**  
   - If the API server cannot be reached or returns status code ≠ 200:  
     ```
     [ Tidak Bisa Terhubung ] 
     URL    : <url>  
     Status : <status_code>
     ```
   - If another error occurs (e.g. timeout, no network):  
     ```
     [ Error ] <detail error>
     ```

3. **Currency not found (LOCAL)**  
   - If the currency code is not available in `rates.json`:  
     ```
     [ Kurs: XXX Tidak Ditemukan ]
     [ Silahkan Masukan Kurs Yang Tersedia ]
     -------------------------------------------------------
     USD : United States Dollar
     IDR : Indonesian Rupiah
     ...
     -------------------------------------------------------
     ```

4. **Currency not found (API)**  
   - If the currency code is invalid in API data:  
     ```
     [ Kurs : XXX Tidak Ditemukan ]
     [ Silahkan Masukan Kurs Yang Tersedia ]
     -------
     | USD |
     | IDR |
     | EUR |
     ...
     -------
     ```

5. **Same currency (no conversion needed)**  
   - If `kurs_awal` = `kurs_akhir`, the program will immediately return the `jumlah` value without conversion.

---

## Code `currency_converter.py`

```python
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
```
