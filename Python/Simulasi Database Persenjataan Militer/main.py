import sqlite3
from time import sleep
from typing import List, Optional, Union, cast

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.style import Style
from rich.table import Table
from rich.text import Text
from rich.theme import Theme


DB_FILE = "persenjataan_militer.db"

theme = Theme({
    "info": "white",
    "accent": "cyan",
    "result": "bold black on cyan",
    "error": "red",
    "highlight": "bold white on red",
})
console = Console(theme=theme)


class Database:
    def __init__(self, db_file: str = DB_FILE):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
                """
            )
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS weapons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_senjata TEXT NOT NULL,
                    tipe_senjata TEXT NOT NULL,
                    tingkat_bahaya TEXT NOT NULL,
                    jumlah_persediaan INTEGER NOT NULL
                )
                """
            )

    def execute(
        self,
        query: str,
        params: tuple = (),
        fetch_one: bool = False,
        fetch_all: bool = False,
    ) -> Union[Optional[sqlite3.Row], List[sqlite3.Row], sqlite3.Cursor]:
        cursor = self.conn.cursor()
        cursor.execute(query, params)

        if fetch_one:
            return cursor.fetchone()
        if fetch_all:
            return cursor.fetchall()
        
        self.conn.commit()
        return cursor

    def close(self):
        self.conn.close()


class Authentication:
    def __init__(self, db: Database) -> None:
        self.db = db
        self.ensure_default_user()

    def ensure_default_user(self) -> None:
        user = self.db.execute("SELECT * FROM users LIMIT 1", fetch_one=True)
        
        if not user:
            self.db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                ("admin", "admin"),
            )
            console.print(
                "[result]> Default user dibuat:[/result]\n"
                " username: admin\n"
                " password: admin\n",
                style="info"
            )
            sleep(2)

    def login(self) -> bool:
        console.rule(
            "Login Sistem Persenjataan Militer",
            style=Style(color="cyan", bold=True)
        )
        
        username = Prompt.ask("Masukkan username")
        password = Prompt.ask("Masukkan password", password=True)
        sleep(1)

        user = self.db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
            fetch_one=True,
        )
        
        if user:
            console.print("> Login sukses", style="result")
            return True
        
        console.print("> Username atau password salah", style="highlight")
        return False


class ArsenalManager:
    def __init__(self, db: Database) -> None:
        self.db = db

    @staticmethod
    def get_danger_level_style(tingkat: str) -> str:
        tingkat_lower = tingkat.lower()
        
        if tingkat_lower == "rendah":
            return "yellow"
        elif tingkat_lower == "sedang":
            return "rgb(255,165,0)"  # orange
        elif tingkat_lower == "tinggi":
            return "red"
        
        return "white"

    def add_weapon(self) -> None:
        console.rule(
            "Tambah Data Senjata",
            style=Style(color="cyan", bold=True)
        )
        
        print()
        nama = Prompt.ask("Nama senjata")
        tipe = Prompt.ask("Tipe senjata")
        tingkat = Prompt.ask("Tingkat bahaya (Rendah/Sedang/Tinggi)", default="Sedang")
        jumlah = Prompt.ask("Jumlah persediaan", default="0")
        
        try:
            self.db.execute(
                """
                INSERT INTO weapons (nama_senjata, tipe_senjata, tingkat_bahaya, jumlah_persediaan)
                VALUES (?, ?, ?, ?)
                """,
                (nama, tipe, tingkat, int(jumlah)),
            )
            console.print("Senjata berhasil ditambahkan ke database", style="accent")
        except Exception as e:
            console.print(f"[highlight]> Gagal menambahkan senjata:[/highlight]\n {e}", style="error")

    def list_weapons(self) -> None:
        console.rule(
            "Daftar Persenjataan Militer",
            style=Style(color="cyan", bold=True)
        )
        
        print()
        result = self.db.execute("SELECT * FROM weapons ORDER BY id", fetch_all=True)
        rows = cast(List[sqlite3.Row], result)
        
        table = Table(
            title="Database Persenjataan Militer",
            box=box.SIMPLE_HEAD,
            header_style="accent",
            border_style="white",
        )
        
        table.add_column("ID", style="info", justify="right")
        table.add_column("Nama Senjata", style="info")
        table.add_column("Tipe", style="info")
        table.add_column("Tingkat Bahaya")
        table.add_column("Jumlah", style="info", justify="right")
        
        if not rows:
            console.print("Belum ada data senjata di database", style="error")
            return
        
        for row in rows:
            danger_style = self.get_danger_level_style(row["tingkat_bahaya"])
            table.add_row(
                str(row["id"]),
                row["nama_senjata"],
                row["tipe_senjata"],
                Text(row["tingkat_bahaya"], style=danger_style),
                str(row["jumlah_persediaan"]),
            )
        console.print(table)

    def update_weapon(self) -> None:
        console.rule(
            "Perbarui Data Senjata", 
            style=Style(color="cyan", bold=True)
        )
        
        print()
        item_id = Prompt.ask("Masukkan ID senjata yang ingin diubah")
        
        item = cast(
            Optional[sqlite3.Row], 
            self.db.execute("SELECT * FROM weapons WHERE id = ?", (item_id,), fetch_one=True)
        )
        
        if not item:
            console.print("Data senjata tidak ditemukan", style="error")
            return
        
        nama = Prompt.ask("Nama senjata", default=item["nama_senjata"])
        tipe = Prompt.ask("Tipe senjata", default=item["tipe_senjata"])
        tingkat = Prompt.ask("Tingkat bahaya", default=item["tingkat_bahaya"])
        jumlah = Prompt.ask("Jumlah persediaan", default=str(item["jumlah_persediaan"]))
        
        try:
            self.db.execute(
                """
                UPDATE weapons
                SET nama_senjata = ?, tipe_senjata = ?, tingkat_bahaya = ?, jumlah_persediaan = ?
                WHERE id = ?
                """,
                (nama, tipe, tingkat, int(jumlah), item_id),
            )
            console.print("Data senjata berhasil diperbarui", style="accent")
        except Exception as e:
            console.print(f"[highlight]> Gagal memperbarui:[/highlight]\n {e}", style="error")

    def delete_weapon(self) -> None:
        console.rule(
            "Hapus Data Senjata", 
            style=Style(color="cyan", bold=True)
        )

        print()
        item_id = Prompt.ask("Masukkan ID senjata yang ingin dihapus")
        
        item = cast(
            Optional[sqlite3.Row], 
            self.db.execute("SELECT * FROM weapons WHERE id = ?", (item_id,), fetch_one=True)
        )
        
        if not item:
            console.print("Data senjata tidak ditemukan", style="error")
            return
        
        confirm = Prompt.ask(
            f"Yakin akan menghapus {item['nama_senjata']}? (y/n)", 
            choices=["y", "n"], 
            default="n"
        )

        if confirm == "y":
            try:
                self.db.execute("DELETE FROM weapons WHERE id = ?", (item_id,))
                console.print("Data senjata berhasil dihapus", style="accent")
            except Exception as e:
                console.print(f"[highlight]> Gagal menghapus:[/highlight]\n {e}", style="error")
        else:
            console.print("Penghapusan dibatalkan", style="accent")

    def search_weapon(self) -> None:
        console.rule(
            "Cari Senjata", 
            style=Style(color="cyan", bold=True)
        )
        
        print()
        keyword = Prompt.ask("Masukkan nama atau tipe untuk mencari")
        
        result = self.db.execute(
            """
            SELECT * FROM weapons
            WHERE nama_senjata LIKE ? OR tipe_senjata LIKE ?
            ORDER BY id
            """,
            (f"%{keyword}%", f"%{keyword}%"),
            fetch_all=True,
        )
        
        rows = cast(List[sqlite3.Row], result)
        if not rows:
            console.print("Tidak ditemukan senjata dengan kata kunci tersebut", style="error")
            return
        
        print()
        table = Table(
            title=f"Hasil Pencarian '{keyword}'",
            box=box.SIMPLE_HEAD,
            header_style="accent",
            border_style="white",
        )
        
        table.add_column("ID", style="info", justify="right")
        table.add_column("Nama Senjata", style="info")
        table.add_column("Tipe", style="info")
        table.add_column("Tingkat Bahaya")
        table.add_column("Jumlah", style="info", justify="right")
        
        for row in rows:
            danger_style = self.get_danger_level_style(row["tingkat_bahaya"])
            table.add_row(
                str(row["id"]),
                row["nama_senjata"],
                row["tipe_senjata"],
                Text(row["tingkat_bahaya"], style=danger_style),
                str(row["jumlah_persediaan"]),
            )
        console.print(table)

    def stock_status(self) -> None:
        console.rule(
            "Status Persediaan Senjata", 
            style=Style(color="cyan", bold=True)
        )
        
        print()
        result = self.db.execute("SELECT * FROM weapons ORDER BY id", fetch_all=True)
        rows = cast(List[sqlite3.Row], result)
        
        if not rows:
            console.print("Belum ada data senjata di database", style="error")
            return
        
        table = Table(
            title="Status Persediaan",
            box=box.SIMPLE_HEAD,
            header_style="accent",
            border_style="white",
        )
        
        table.add_column("ID", style="info", justify="right")
        table.add_column("Nama Senjata", style="info")
        table.add_column("Jumlah", style="info", justify="right")
        table.add_column("Tingkat Bahaya")
        
        for row in rows:
            danger_style = self.get_danger_level_style(row["tingkat_bahaya"])
            table.add_row(
                str(row["id"]),
                row["nama_senjata"],
                str(row["jumlah_persediaan"]),
                Text(row["tingkat_bahaya"], style=danger_style),
            )
        console.print(table)

class Menu:
    def __init__(self, auth: Authentication, arsenal: ArsenalManager) -> None:
        self.auth = auth
        self.arsenal = arsenal

    def show(self) -> None:
        if not self.auth.login():
            return
        
        while True:
            sleep(2)
            print("\n")

            menu_text = Text.from_markup(
                "[accent][1][/accent] Tambah Senjata\n"
                "[accent][2][/accent] Lihat Semua Senjata\n"
                "[accent][3][/accent] Update Senjata\n"
                "[accent][4][/accent] Hapus Senjata\n"
                "[accent][5][/accent] Cari Senjata\n"
                "[accent][6][/accent] Status Persediaan\n"
                "[accent][7][/accent] Keluar"
            )
            
            console.print(
                Panel(
                    menu_text,
                    title="[bold cyan]Menu Persenjataan Militer[/bold cyan]",
                    title_align="center",
                    style=Style(color="white"),
                    border_style="white",
                )
            )
            
            choice = Prompt.ask("Pilih menu", choices=[str(i) for i in range(1, 8)])
            print("\n")
            sleep(1)
            
            match choice:
                case "1":
                    self.arsenal.add_weapon()
                case "2":
                    self.arsenal.list_weapons()
                case "3":
                    self.arsenal.update_weapon()
                case "4":
                    self.arsenal.delete_weapon()
                case "5":
                    self.arsenal.search_weapon()
                case "6":
                    self.arsenal.stock_status()
                case "7":
                    console.print("> Keluar dari program", style="result")
                    sleep(2)
                    break

def main():
    db = Database()
    auth = Authentication(db)
    arsenal = ArsenalManager(db)
    menu = Menu(auth, arsenal)
    
    try:
        menu.show()
    except KeyboardInterrupt:
        console.print("\nProgram dihentikan oleh pengguna", style="error")
    finally:
        db.close()

if __name__ == "__main__":
    main()