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

