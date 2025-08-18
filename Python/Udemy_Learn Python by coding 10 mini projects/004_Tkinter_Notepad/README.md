# Tkinter Notepad

A simple **Notepad application** built with Python's `tkinter` library.  
It allows users to write, save, and load `.txt` files with a dark-themed interface.

## Features

- Minimalist text editor built with `tkinter`.  
- Supports **saving** text to `.txt` files.  
- Supports **loading** existing `.txt` files.  
- Dark theme interface for better readability.  
- Window automatically centered on the screen.  
- Error messages and success notifications via message dialogs.

## Notes

- ‼️This code is mostly written in Indonesian (function names, variables, prompts, and comments). Non-Indonesian speakers might need additional effort to read or modify the code.  
- Only `.txt` files are supported.  
- Suitable for small text editing tasks, not a full-featured editor.  

## Requirements

- Python 3.x  
- Standard library only (`tkinter` is included with Python).  

---

## Usage

1. Run the script on your terminal or command-line interface:

   ```bash
   python tkinter_notepad.py
   ```

2. After launching, a window will appear featuring:
   - A **dark-themed text area**, where you can type or paste your notes.
   - A toolbar containing two buttons:
     - **Save**: Save the current text as a `.txt` file. If the note was loaded from an existing file, it will overwrite that file. Otherwise, you’ll be prompted to choose a save location and filename.
     - **Load**: Open an existing `.txt` file and load its contents into the text area.

3. When clicking **Save** or **Load**, the app displays a dialog:
   - On success: a pop-up with the message like `File saved to: <path>` or `File loaded from: <path>`.
   - On error: an error dialog showing `File Gagal Di-save` or `File Gagal Di-load` along with details.

4. To exit the app, simply close the window.

### Platform Notes

- **Windows & macOS**: Just run the script directly in your terminal—no extra setup needed.
- **Linux (GUI available)**: Run via terminal as above.
- **Headless or remote Linux without GUI display**: You must first set up display forwarding:
  ```bash
  export DISPLAY=:0
  python tkinter_notepad.py
  ```

---

## Example Output

### 1. Initial Window
When you run the script, the application starts with:

- A **blank text area** (dark background, white text)  
- Two buttons: **Save** and **Load**  
- The window is centered on screen

_(preview on Pydroid3)_

<img src="https://github.com/NaN-code01/Small_Projects_Collection/blob/main/Python/Udemy_Learn%20Python%20by%20coding%2010%20mini%20projects/004_Tkinter_Notepad/images/Screenshot_01.jpg" alt="app screenshot" width="250">

### 2. After Saving a File
A pop-up appears:

```
File saved
File saved to: C:/Users/NaN/Documents/note.txt
```

### 3. After Loading a File
A pop-up appears:

```
File loaded
File loaded from: C:/Users/NaN/Documents/note.txt
```

### 4. Error on Saving
If saving fails (e.g., permission denied):

```
File Gagal Di-save
Details: [Errno 13] Permission denied: 'C:/restricted_folder/note.txt'
```

### 5. Error on Loading
If loading fails (e.g., file not found):

```
File Gagal Di-load
Details: [Errno 2] No such file or directory: 'missing.txt'
```

---

## Code `tkinter_notepad.py`

```python
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
export DISPLAY=:1;
python tkinter_notepad.py
'''
```
