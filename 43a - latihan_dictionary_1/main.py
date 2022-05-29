# 43a - Latihan Dictionary
import datetime
import os

# Template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 1)
}
data_mahasiswa = {}

# os.system("clear")
os.system("cls")

print("=" * 20)
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("=" * 20)

# fromkeys ->
mahasiswa = dict.fromkeys(mahasiswa_template.keys())

mahasiswa['nama'] = input("Nama Mahasiswa\t: ")
mahasiswa['nim'] = input("NIM Mahasiswa\t: ")
mahasiswa['sks_lulus'] = input("SKS Lulus\t: ")
TAHUN_LAHIR = int(input("Tahun Lahir [yyyy]: "))
BULAN_LAHIR = int(input("Bulan Lahir [1-12]: "))
TANGGAL_LAHIR = int(input("Tanggal Lahir [1-31]: "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)
