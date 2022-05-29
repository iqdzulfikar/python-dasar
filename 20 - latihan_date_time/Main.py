# 20 - Date and Time (Latihan)
import datetime as dt

print("Silahkan masukkan Tanggal lahir Anda")
tanggal = int(input("Tanggal\t: "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal Lahir Anda: {tanggal_lahir}")

hari_ini = dt.date.today()
print(hari_ini)

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
print(f"Harinya adalah: {tanggal_lahir:%A}")
print(f"Umur Anda adalah= {umur_tahun} tahun, {umur_bulan} bulan")
