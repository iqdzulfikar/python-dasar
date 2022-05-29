# 42 - Multi keys Nesting Dictionary
import datetime

mahasiswa_1 = {
    'nama': 'Ucup Surucup',
    'nim': '19111025',
    'sks': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 3, 11)
}

mahasiswa_2 = {
    'nama': 'Otong Surotong',
    'nim': '19111026',
    'sks': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2000, 9, 6)
}

mahasiswa_3 = {
    'nama': 'Asep si kasyep',
    'nim': '19111027',
    'sks': 100,
    'beasiswa': False,
    'lahir': datetime.datetime(1999, 9, 4)
}

data_mahasiswa = {
    'MAH001': mahasiswa_1, 'MAH002': mahasiswa_2, 'MAH003': mahasiswa_3
}
print(f"{'KEY':^6} {'NAMA':^17} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':^10}")
print("=" * 50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")  # bulan/tanggal/tahun

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")
