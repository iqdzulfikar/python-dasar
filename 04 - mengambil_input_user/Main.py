# Mengambil input data dari user

# data yang di masukkan pasti string
data = input("Masukkan Angka: ")
print("data = ", data, ", type = ", type(data))

# jika mengambil data int
data_int = int(input("\n\nMasukkan Angka: "))
print("data = ", data_int, ", type = ", type(data_int))

# ambil data float
data_float = float(input("Masukkan Angka: "))
print("data = ", data_float, ", type = ", type(data_float))

# ambil data bool (boolean)
data_boolean = bool(input("Masukkan Angka: "))
print("data = ", data_boolean, ", type = ", type(data_boolean))