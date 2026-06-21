# Simulasi Database Persenjataan Militer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Library](https://img.shields.io/badge/Library-Rich-cyan)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

> **Simulasi Database Persenjataan Militer** adalah aplikasi **Command Line Interface (CLI)** berbasis Python yang digunakan untuk mengelola data persenjataan secara terstruktur menggunakan SQLite.  
> Program ini mendukung proses **login**, **tambah data**, **lihat data**, **ubah data**, **hapus data**, **pencarian**, dan **pemantauan status persediaan**.

---

## 📌 Tautan Dokumentasi YouTube



```text
https://youtu.be/9IiWFpHivpo
```

---

## ✨ Fitur Program

- **Autentikasi pengguna** dengan akun default `admin / admin`.
- **Tambah data senjata** ke database.
- **Menampilkan seluruh data senjata** dalam bentuk tabel.
- **Memperbarui data senjata** berdasarkan ID.
- **Menghapus data senjata** berdasarkan ID.
- **Mencari senjata** berdasarkan nama atau tipe.
- **Menampilkan status persediaan** senjata.
- **Pewarnaan tampilan terminal** menggunakan library `rich` agar output lebih informatif dan mudah dibaca.

---

## 🧰 Dependensi

Program ini menggunakan pustaka berikut:

- `sqlite3` → sudah tersedia bawaan Python.
- `rich` → untuk tampilan antarmuka terminal yang lebih menarik.
- `time.sleep` → untuk jeda tampilan pada beberapa bagian program.

---

## ⚙️ Cara Instalasi

### 1. Pastikan Python telah terpasang

Program membutuhkan **Python 3.10 atau lebih baru** karena menggunakan fitur `match-case`.

Periksa versi Python:

```bash
python --version
```

### 2. Pastikan file program tersedia

Pastikan file berikut berada dalam satu direktori proyek:

```text
main.py
```

### 3. Instal dependensi

Instal library yang diperlukan:

```bash
pip install rich
```

> Jika menggunakan `pip3`, sesuaikan perintah dengan konfigurasi sistem yang digunakan.

### 4. Jalankan program

```bash
python main.py
```

### 5. Login ke sistem

Saat pertama kali dijalankan, program akan membuat akun bawaan:

```text
Username: admin
Password: admin
```

Gunakan akun tersebut untuk mengakses menu utama aplikasi.

---

## 🖥️ Penjelasan Program

Program ini memiliki struktur utama sebagai berikut:

### 1. `Database`
Kelas ini bertugas mengelola koneksi ke database SQLite bernama `persenjataan_militer.db`.  
Di dalam kelas ini juga dibuat dua tabel utama, yaitu:

- `users` → menyimpan data pengguna untuk login.
- `weapons` → menyimpan data persenjataan.

### 2. `Authentication`
Kelas ini menangani proses autentikasi pengguna.  
Apabila database belum memiliki akun, program akan membuat akun default secara otomatis:

- **Username:** `admin`
- **Password:** `admin`

### 3. `ArsenalManager`
Kelas ini mengelola seluruh operasi utama terhadap data senjata, antara lain:

- menambah data senjata,
- menampilkan seluruh data,
- memperbarui data,
- menghapus data,
- mencari data,
- menampilkan status persediaan.

### 4. `Menu`
Kelas ini berfungsi menampilkan menu utama dan mengarahkan pengguna ke fitur yang dipilih.

### 5. `main()`
Fungsi utama yang menjalankan program, menghubungkan database, membuat objek autentikasi, dan memulai menu aplikasi.

---

## 🧩 Alur Penggunaan Program

1. Program dijalankan.
2. Sistem menampilkan halaman login.
3. Pengguna memasukkan username dan password.
4. Jika login berhasil, menu utama akan tampil.
5. Pengguna dapat memilih salah satu menu berikut:
   - tambah data senjata,
   - lihat semua data,
   - update data,
   - hapus data,
   - cari data,
   - lihat status persediaan,
   - keluar dari program.

---

## 📤 Penjelasan Output Program

### 1. Output Login
Saat program dimulai, pengguna akan diminta untuk memasukkan username dan password.  
Jika berhasil masuk, program menampilkan pesan:

```text
> Login sukses
```

Jika gagal, program menampilkan pesan:

```text
> Username atau password salah
```

### 2. Output Saat Menambah Data
Setelah data berhasil disimpan, program akan menampilkan pesan:

```text
Senjata berhasil ditambahkan ke database
```

### 3. Output Saat Menampilkan Data
Data senjata ditampilkan dalam bentuk tabel yang memuat:

- ID
- Nama Senjata
- Tipe
- Tingkat Bahaya
- Jumlah Persediaan

Tingkat bahaya diberi warna berbeda agar lebih mudah dibedakan:
- **Rendah** → kuning
- **Sedang** → oranye
- **Tinggi** → merah

### 4. Output Saat Update Data
Jika pembaruan berhasil, program menampilkan pesan:

```text
Data senjata berhasil diperbarui
```

### 5. Output Saat Menghapus Data
Jika penghapusan berhasil, program menampilkan pesan:

```text
Data senjata berhasil dihapus
```

Jika pengguna membatalkan, program menampilkan:

```text
Penghapusan dibatalkan
```

### 6. Output Saat Pencarian
Hasil pencarian akan ditampilkan dalam tabel.  
Jika tidak ditemukan data yang sesuai, program menampilkan pesan:

```text
Tidak ditemukan senjata dengan kata kunci tersebut
```

### 7. Output Status Persediaan
Menu ini menampilkan ringkasan jumlah persediaan setiap senjata dalam tabel khusus.  
Fitur ini berguna untuk memantau stok senjata secara cepat.

---

## 📁 Struktur Data Database

### Tabel `users`
| Kolom | Keterangan |
|------|------------|
| `id` | ID pengguna |
| `username` | Nama pengguna |
| `password` | Kata sandi |

### Tabel `weapons`
| Kolom | Keterangan |
|------|------------|
| `id` | ID senjata |
| `nama_senjata` | Nama senjata |
| `tipe_senjata` | Jenis atau kategori senjata |
| `tingkat_bahaya` | Level bahaya senjata |
| `jumlah_persediaan` | Jumlah stok yang tersedia |

---

## 📌 Catatan Penting

- Program ini merupakan **simulasi** berbasis terminal, bukan sistem operasional nyata.
- Data disimpan secara lokal pada file database `persenjataan_militer.db`.
- Jika file database dihapus, maka data yang tersimpan juga akan hilang.
- Untuk keamanan, kredensial sebaiknya tidak menggunakan sistem default pada penggunaan produksi.

---

## 🛠️ Contoh Penggunaan

### Login
```text
username: admin
password: admin
```

### Menambah Senjata
```text
Nama senjata: AK-47
Tipe senjata: Assault Rifle
Tingkat bahaya: Tinggi
Jumlah persediaan: 12
```

---
