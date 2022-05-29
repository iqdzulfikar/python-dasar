# 43b - Latihan Dictionary Part 2
import datetime
import os
import string
import random

# Template dict mahasiswa
mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 1)
}
data_mahasiswa = {}

while True:
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
    mahasiswa['lahir'] = datetime.datetime(
        TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_mahasiswa.update({KEY: mahasiswa})

    print(f"\n{'Key':^10} {'Nama Mahasiswa':^20} {'NIM':^12} {'SKS Lulus':^10} {'Tanggal Lahir':^16}")
    print("="*75)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")  # bulan/tanggal/tahun

        print(f"{KEY:^10} {NAMA:<20} {NIM:<12} {SKS:^10} {LAHIR:>16}")

    print("\n")

    is_done = input("Mau tambah lagi bro[y/n]? ")
    if is_done == "n":
        break

print("\nAkhir dari program.\nTerima kasih")
