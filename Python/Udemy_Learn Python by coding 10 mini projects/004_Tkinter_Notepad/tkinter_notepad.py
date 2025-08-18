#[ Python ]

# Import modul penting
import tkinter as tk 
from tkinter import filedialog as fd
from tkinter import messagebox as msb

# Class notepad
class Notepad:
  # inisialisasi class
  def __init__(self, root: tk.Tk) -> None:
    self.root = root
    self.root.title('Notepad')
    self.center_window()
    
    # bikin teks area box (buat diisi)
    self.text_area: tk.Text = tk.Text(
      self.root,
      wrap='word',
      bg='#1e1e1e',
      fg='white',
      insertbackground='white',
      highlightbackground='#151515',
      highlightcolor='white',
      bd=0
      )
    self.text_area.pack(expand=True, fill='both')
    
    # bikin frame buat tombol
    self.frame_tombol: tk.Frame = tk.Frame(self.root, bg='#3e3e3e')
    self.frame_tombol.pack(pady=2)
    
    # tombol save 
    self.file_path = None
    self.tombol_save: tk.Button = tk.Button(
      self.frame_tombol, text='Save', command=self.save_file,
      bg='#1e1e1e', fg='white')
    self.tombol_save.pack(side=tk.LEFT)
    
    # tombol load  
    self.tombol_load: tk.Button = tk.Button(
      self.frame_tombol, text='Load', command=self.load_file,
      bg='#1e1e1e', fg='white')
    self.tombol_load.pack(side=tk.LEFT)
  
  # fungsi save file 
  def save_file(self) -> None:
    try:
      # save file nya
      if self.file_path: # kalau file dibuka dari load (save ke file yg sudah ada)
        with open(self.file_path, 'w') as file:
          file.write(self.text_area.get(1.0, tk.END))
        print(f'\nFile tersimpan ke : {self.file_path}')
        msb.showinfo('Berhasil Menyimpan File', f'File tersimpan ke : {self.file_path}')
      else: # kalau file baru (bikin file baru)
        file_path: str = fd.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
        if file_path:
          with open(file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))
          self.file_path = file_path
          print(f'\nFile tersimpan ke : {file_path}')
          msb.showinfo('Berhasil Menyimpan File', f'File tersimpan ke : {file_path}')
    except Exception as e:
      print(f'\nGagal save file:\n{e}')
      msb.showerror(
        'File Gagal Di-save',
        f'Detail : {e}')
  
  # fungsi load file
  def load_file(self) -> None:
    try:
      file_path: str = fd.askopenfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')])
      if file_path:
        # load file nya
        with open(file_path, 'r') as file:
          konten: str = file.read()
          self.text_area.delete(1.0, tk.END)       # clear area
          self.text_area.insert(tk.INSERT, konten) # load konten baru
        self.file_path = file_path # nyimpen path yg di load
        print(f'\nFile di-load dari : {file_path}')
    except Exception as e:
      print(f'\nGagal load file:\n{e}')
      msb.showerror(
        'File Gagal Di-load',
        f'Detail : {e}')
  
  # fungsi center (bawa ke tengah)
  def center_window(self, width: int = 600, height: int = 400) -> None:
    layar_lebar = self.root.winfo_screenwidth()
    layar_tinggi = self.root.winfo_screenheight()

    x = (layar_lebar // 2) - (width // 2)
    y = (layar_tinggi // 2) - (height // 2)

    self.root.geometry(f'{width}x{height}+{x}+{y}')
  
  # fungsi run program 
  def run(self) -> None:
    self.root.mainloop()

# Main entry
def main() -> None:
  root: tk.Tk = tk.Tk()
  app: Notepad = Notepad(root=root)
  app.run()

# Run
if __name__ == '__main__':
  main()

'''
export DISPLAY=:11;
python tkinter_notepad.py
'''