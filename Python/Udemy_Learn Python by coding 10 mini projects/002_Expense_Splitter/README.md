# Expense Splitter

A Python script to split expenses among multiple people either **equally** or based on a **percentage contribution**.

## Features

- Split bills evenly among participants.
- Split bills based on custom percentages.
- Validates user input (bill amount, number of people, percentages).
- Automatically adjusts the last person's percentage to ensure the total is always 100%.
- Supports custom currency symbols.

## Notes

- ‼️This code is mostly written in Indonesian (variable names, prompts, and comments). Users who are not familiar with the Indonesian language may find it harder to read or modify.
- The script requires all numeric inputs to be positive values.
- When choosing percentage-based splitting, the program ensures the total contribution is exactly 100%.
- Currency symbol can be changed by editing the `mata_uang` parameter in the `hitung_patungan` function (default: `Rp` → Indonesian Rupiah).

## Requirements

- Python 3.x

---

## Usage

1. Run the script in your terminal:

```bash
python expense_splitter.py
```

2. The program will ask you to input the following:

- **Total Bill** (`Tagihan`)  
  Example: `500000`  
  > The total expense to be split.

- **Number of People** (`Banyak Orang`)  
  Example: `3`  
  > The total number of participants.  
  (Must be greater than 1)

- **Split Method**  
  - `[a]` Equal Split (`Bagi Rata`)  
    Everyone pays the same amount.  
  - `[b]` Percentage Split (`Bagi Dengan Persentase`)  
    Each participant pays according to their chosen percentage.  
    The last participant automatically gets the remaining percentage.

3. Input participant names and their percentage (if using percentage split).  
   - If the name is left blank → it defaults to a number (e.g., "1", "2", etc.).  
   - Names longer than 10 characters are not allowed.  
   - Percentage must be greater than 0 and total ≤ 100%.

4. The program will display:  
- Total Bill  
- Number of People  
- Individual contribution (equal or percentage-based)

---

## Example Output

### Equal Split (`[a] Bagi Rata`)

```bash
----------------------------------------
Total Tagihan : Rp500,000.00
Banyak Orang  : 3
--------------------
Patungan/Orang: Rp166,666.67
----------------------------------------
```

### Percentage Split (`[b] Bagi Dengan Persentase`)

```bash
----------------------------------------
Bagi Persentase
----------------------------------------

Orang ke-1: Arif
Si-Arif bayar brp% [angka]: 40

Orang ke-2: Budi
Si-Budi bayar brp% [angka]: 30

Orang ke-3: Cecep
Si-Cecep bayar sisa% : 30
----------------------------------------

----------------------------------------
Total Tagihan : Rp500,000.00
Banyak Orang  : 3
--------------------
List Patungan/Orang
Arif    [40 %]: Rp200,000.00
Budi    [30 %]: Rp150,000.00
Cecep   [30 %]: Rp150,000.00
----------------------------------------
```

---

## Error Handling

The program includes several validations and error messages:

- **Invalid input (non-numeric values)**  
  ```bash
  [ input yg bener ]
  ```
  → Shown when entering letters/symbols instead of numbers.

- **Bill amount = 0**  
  ```bash
  [ tagihan Rp0 mah gausah di bayar ]
  ```
  → Bill of Rp0 does not make sense.

- **Bill amount < 0**  
  ```bash
  [           tagihan harus > 0            ]
  [ ini toko nya hutang ke lu apa gmn dah? ]
  ```
  → Negative bills are rejected.

- **Number of people = 1**  
  ```bash
  [ kalo sendiri ya bayar sendiri aja jir ]
  ```
  → Splitting does not apply if only one person.

- **Number of people < 1**  
  ```bash
  [ awowkawowk orang nya pada kabur ]
  ```
  → Invalid if less than 1 person.

- **Percentage ≤ 0%**  
  ```bash
  [ persentase jangan <= 0% ]
  ```
  → Each participant’s share must be greater than 0%.

- **Total percentage > 100%**  
  ```bash
  [ persentase jangan melebihi 100% ]
  [   nanti sisanya malah ga bayar  ]
  ```
  → Prevents exceeding 100% total contribution.

---

## Code `expense_splitter.py`

```python
#[ Python ]

# Fungsi menghitung patungan
def hitung_patungan(tagihan: float, banyak_orang: int, metode_bagi: str, mata_uang: str):
  
  # Hitungan 
  if metode_bagi == 'b': # Metode [b]
    
    # Fungsi rapihin spasi
    def hollow(nama: str, panjang: int):
      spasi: str = ' ' * (panjang - len(str(nama)))
      if isinstance(nama, float):
        return f'{spasi}{nama:,.0f}'
      else:
        return f'{nama}{spasi}'
    
    # Fungsi list patungan
    def patungan_persentase():
      # Cek nama terpanjang
      panjang: int = 0
      for n in range(len(NAMA)):
        if len(NAMA[n]) > panjang:
          panjang: int = len(NAMA[n])
      # Tampilan list
      for i in range(len(NAMA)):
        patungan_masing2: float = tagihan * (float(data_patungan[NAMA[i]]) / 100)
        print(f'{hollow(NAMA[i], panjang)} [{hollow(data_patungan[NAMA[i]], 4)}%]: {mata_uang}{patungan_masing2:,.2f}')
    
    # Fungsi persentase sebelum
    def persentase_sebelum():
      persentase_sebelumnya: float = 0
      if len(NAMA) > 0:
        for i in range(len(NAMA)):
          persentase_sebelumnya += float(data_patungan[NAMA[i]])
      return float(persentase_sebelumnya)
    
    print(f"{'-'*40}")
    print('Bagi Persentase')
    
    # dict & list kosong buat nyimpen persentase
    data_patungan: dict = {}
    NAMA: list = []
    
    # Input nama dan persentase masing-masini
    for orang in range(banyak_orang):
      
      # Handle input nama 
      while True:
        try:
          nama: str = input(f'\nOrang ke-{orang+1}: ')
          if nama == '':
            nama = str(orang+1)
            break
          elif len(str(nama)) > 10:
            print('\n[ namanya jangan terlalu panjang ]')
          elif len(str(nama)) <= 0:
            print('\n[ kasih nama yg bener ]')
          else:
            break
        except Exception:
          print('\n[ ERROR ]')
      
      # input persentase
      if orang == banyak_orang-1:
        persentase: float = float(100 - persentase_sebelum())
        print(f'Si-{nama} bayar sisa% : {persentase:,.0f}')
      else:
        # Handle input persentase
        while True:
          try:
            persentase: float = float(input(f'Si-{nama} bayar brp% [angka]: '))
            if (persentase + persentase_sebelum() < 100) and (persentase > 0):
              break
            elif persentase <= 0:
              print('\n[ persentase jangan <= 0% ]\n')
            else:
              print('\n[ persentase jangan melebihi 100% ]')
              print('[   nanti sisanya malah ga bayar  ]\n')
          except ValueError:
            print('\n[ input yg bener ]\n')
      
      data_patungan[nama] = persentase
      NAMA: list = list(data_patungan.keys())
      
    print(f"{'-'*40}\n")
    
  else: # Metode [a]
    patungan_perorang: float = tagihan / banyak_orang
  
  # Output string
  print('-'*40)
  
  print(f'Total Tagihan : {mata_uang}{tagihan:,.2f}')
  print(f'Banyak Orang  : {banyak_orang}')
  
  print('-'*20)
  
  if metode_bagi == 'b':
    print('List Patungan/Orang')
    patungan_persentase()
  else:
    print(f'Patungan/Orang: {mata_uang}{patungan_perorang:,.2f}')
  
  print('-'*40)

# Main katanya
def main():
  print('-'*40)
  
  # Handle Input Awal
  while True:
    try:
      # Handle input tagihan
      while True:
        tagihan: float = float(input('Brp Tagihan Total? [angka]: Rp'))
        if tagihan > 0:
          break
        elif tagihan == 0:
          print('\n[ tagihan Rp0 mah gausah di bayar ]\n')
        else:
          print('\n[           tagihan harus > 0            ]')
          print('[ ini toko nya hutang ke lu apa gmn dah? ]\n')
      # Handle input banyak orang 
      while True:
        banyak_orang: int = int(input('Ada Brp Orang?     [angka]: '))
        if banyak_orang > 1:
          break
        elif banyak_orang == 1:
          print('\n[ kalo sendiri ya bayar sendiri aja jir ]\n')
        else:
          print('\n[ awowkawowk orang nya pada kabur ]\n')
    except ValueError:
      print('\n[ input yg bener ]\n')
    else:
      break
  
  # Handle Metode Bagi 
  if banyak_orang > 2:
    while True:
      try:
        metode_bagi: str = input('\n[a] Bagi Rata\n[b] Bagi Dengan Persentase\nPilih Metode Bagi    [a/b]: ').lower()
        if metode_bagi in ['a', 'b', '']:
          break
        else:
          print('\n[ input yg bener ]')
      except ValueError:
        print('\n[ input yg bener ]')
  else:
    metode_bagi: str = 'a'
  
  print(f"{'-'*40}\n")
  
  # Panggil fungsi menghitung
  hitung_patungan(tagihan, banyak_orang, metode_bagi, mata_uang='Rp')

if __name__ == '__main__':
  main()

'''
python expense_splitter.py
'''
```
