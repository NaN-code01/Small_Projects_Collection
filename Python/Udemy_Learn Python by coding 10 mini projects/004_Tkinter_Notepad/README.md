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

```
 -------------------------------
|           Notepad             |
| ----------------------------- |
| [ Text area - empty ]         |
|                               |
|                               |
| [ Save ]    [ Load ]          |
 -------------------------------
```

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

