#[ Python ]

# Fungsi Kalkulasi
def kalkulasi_keuangan(pendapatan_perbulan: float, pajak: float, pengeluaran: float, mata_uang: str) -> None:
  # Kalkulasi masing-masing
  pajak_perbulan: float = pendapatan_perbulan * (pajak/100)
  pendapatan_bersih_perbulan: float = pendapatan_perbulan - pajak_perbulan - pengeluaran
  
  pendapatan_pertahun: float = pendapatan_perbulan * 12
  pajak_pertahun: float = pajak_perbulan * 12
  pendapatan_bersih_pertahun: float = pendapatan_pertahun - pajak_pertahun - (pengeluaran*12)
  
  # Output string
  print('-'*48)
  print(f'Pajak                     : {pajak:,.0f}%')
  print(f'Pengeluaran Perbulan      : {mata_uang}{pengeluaran:,.2f}\n')
  print(f'Pendapatan Perbulan       : {mata_uang}{pendapatan_perbulan:,.2f}')
  print(f'Pajak Perbulan            : {mata_uang}{pajak_perbulan:,.2f}')
  print(f'Pendapatan Bersih Perbulan: {mata_uang}{pendapatan_bersih_perbulan:,.2f}\n')
  print(f'Pendapatan Pertahun       : {mata_uang}{pendapatan_pertahun:,.2f}')
  print(f'Pajak Pertahun            : {mata_uang}{pajak_pertahun:,.2f}')
  print(f'Pendapatan Bersih Pertahun: {mata_uang}{pendapatan_bersih_pertahun:,.2f}')
  print('-'*48)

# Maint Entry Point
def main() -> None:
  # User input
  while True:
    print('-'*48)
    try:
      pendapatan_perbulan: float = float(input('Masukan pendapatan/bulan  [angka]: '))
      pajak: float = float(input('Masukan %pajak            [angka]: '))
      pengeluaran: float = float(input('Masukan pengeluaran/bulan [angka]: '))
    except ValueError:
      print(f'{"-"*48}\n[input yg bener]\n')
    else:
      if pendapatan_perbulan > 0 and pajak >= 0 and pengeluaran >= 0:
        print(f'{"-"*48}\n')
        break
      else:
        print(f'{"-"*48}\n[input nilai positif]\n')
  
  # Manggil Fungsi Kalkulasi
  kalkulasi_keuangan(pendapatan_perbulan, pajak, pengeluaran, mata_uang='Rp')

# Jalanin sc 
if __name__ == '__main__':
  main()

'''
python finance_calculator.py
'''