# Finance Calculator

A simple Python script to calculate monthly and yearly income, tax, and net income based on user input.

## Features

- Calculates monthly tax and net income.
- Calculates yearly income, tax, and net income.
- Supports custom currency symbols.
- Validates user input to ensure only positive numbers are accepted.

## Notes

- The program requires all inputs to be positive numbers.
- Currency symbol can be changed by editing the function parameter `mata_uang` in the `kalkulasi_keuangan` function.

## Warning

⚠️ This code is mostly written in Indonesian (variable names, prompts, and comments). Users who are not familiar with the Indonesian language may find it harder to read or modify the code.

## Requirements

- Python 3.x

## Usage

1. Run the script in your terminal:

```bash
python finance_calculator.py
```

2. The program will ask you to input the following values:

- **Pendapatan/bulan** → (Monthly Income)  
  Example: `10000000`  
  > Your total income per month.

- **%Pajak** → (Tax Percentage)  
  Example: `10`  
  > The percentage of tax applied to your monthly income.  
  Input as a number only (e.g., `10` means 10%).

- **Pengeluaran/bulan** → (Monthly Expenses)  
  Example: `2000000`  
  > Your total expenses per month.

3. The program will validate your input:  
- If you enter non-numeric values → it will show `[input yg bener]`. -> `"[enter a valid input]"`
- If you enter zero or negative values → it will show `[input nilai positif]`. -> `"[enter positive values]"`

4. Once all inputs are valid, the program will display:  
- Monthly Income, Tax, and Net Income  
- Yearly Income, Tax, and Net Income  

All results are displayed with a currency symbol (default: `Rp` -> Indonesian Rupiah).

## Example Output

```bash
------------------------------------------------
Pajak                     : 10%
Pengeluaran Perbulan      : Rp2,000,000.00

Pendapatan Perbulan       : Rp10,000,000.00
Pajak Perbulan            : Rp1,000,000.00
Pendapatan Bersih Perbulan: Rp7,000,000.00

Pendapatan Pertahun       : Rp120,000,000.00
Pajak Pertahun            : Rp12,000,000.00
Pendapatan Bersih Pertahun: Rp84,000,000.00
------------------------------------------------
```
