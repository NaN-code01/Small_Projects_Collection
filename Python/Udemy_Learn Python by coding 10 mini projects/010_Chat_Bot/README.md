# Chat Bot  

A Python script for a simple **interactive chatbot** that can respond to user inputs, tell the current time, and fetch live **weather forecasts** from BMKG’s public API.  

## Features  

- Responds to basic user inputs with predefined answers.  
- Uses **fuzzy string matching** (SequenceMatcher) to detect the closest response.  
- Responds with the current **time**.  
- Fetches **weather forecasts** from **BMKG API** (Indonesia).  
- Caches weather results to avoid repeated API calls.  
- Ends the program when user says a goodbye phrase.  
- Uses colored terminal output with ANSI escape codes (`\033`).  

## Notes  

- ‼️The code is mostly written in **Indonesian** (variable names, comments, and bot replies).  
- Requires an **internet connection** for weather requests.  
- Weather API: **BMKG open API** (no API key needed).  
- Fuzzy matching threshold: similarity must be at least **50%** to be accepted.  
- Special commands:  
  - `GET_TIME` → replaced with current time.  
  - `GET_CUACA` → replaced with BMKG forecast.  

## Requirements  

- Python 3.x  
- Libraries:  
  - `requests`  
  - `difflib` (built-in)  
  - `datetime` (built-in)  
  - `time` (built-in)  

Install the external dependency with:  

```bash
pip install requests
```

---

## Usage

1. Run the script:

```bash
python chat_bot.py
```

2. The bot will greet you:

```
----------------------------------------
              [ Chat Bot ]
----------------------------------------
Halo... Namaku Bot, mo ngapain?
```

3. Type an input and get a response. Examples:

- Basic reply
```
Input: halo
-----
Bot: Hai! (100.00%)
```

- Ask the time
```
Input: jam berapa?
-----
Bot: Jam sekarang: 14:32 (100.00%)
```

- Weather forecast
```
Input: cuaca sekarang?
-----
Bot:
------------------------------
Lokasi : Kecamatan Serang, Kota Serang, Banten
------------------------------
Cuaca            : Cerah
Suhu Udara       : 32℃
Kelembapan Udara : 60%
Tutupan Awan     : 20%
Curah Hujan      : 0 mm
Kecepatan Angin  : 10 Km/jam
Waktu Perkiraan  : 2025-08-22 15:00
Update Terakhir  : 2025-08-22 08:00
------------------------------
 (100.00%)
```

- Exit
```
Input: selamat tinggal
-----
Bot: Sampai jumpa lagi. (100.00%)

[ Program Selesai ]
```

---

## Error Handling

- If the API request fails → prints `[ ERROR ]` or a status code message.
- If input doesn’t match → bot replies with:
  ```bash
  Bot: Ga paham, coba ketik yg lain
  ```
- If weather data is missing → shows:
  ```bash
  Data prakiraan tidak ditemukan.
  ```

---

## Code `chat_bot.py`

```python

```
