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
Si-Alice bayar brp% [angka]: 40

Orang ke-2: Budi
Si-Bob bayar brp% [angka]: 30

Orang ke-3: Cecep
Si-Charlie bayar sisa% : 30
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
  → Negative bills are rejected with a humorous message.

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

