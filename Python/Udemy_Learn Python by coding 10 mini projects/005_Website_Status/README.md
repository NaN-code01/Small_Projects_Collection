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
