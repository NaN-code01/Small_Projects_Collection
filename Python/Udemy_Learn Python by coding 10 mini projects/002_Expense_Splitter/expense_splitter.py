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