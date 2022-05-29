# 31 - Manipulasi List
data_angka = [1, 5, 1, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka}")


# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")


# ambil posisi data (index dari suatu list)
data = ["Ucup", "Otong", "Dudung", "Ujang"]
index_dudung = data.index("Dudung")
index_ujang = data.index("Ujang")

print(f"Index si Ujang ada di -> {index_ujang}")
print(f"Index si Dudung ada di -> {index_dudung}")


# mengurutkan list (sorting list)
## ascending
print(f"Data angka sebelum sort -> \n{data_angka}")
data_angka.sort()
print(f"data angka setelah sort -> \n{data_angka}")
print(f"Data sebelum sort -> \n{data}")
data.sort()
print(f"data setelah sort -> \n{data}")

# descending
data_angka.reverse()
print(f"data angka setelah reverse -> \n{data_angka}")
data.reverse()
print(f"data setelah sort -> \n{data}")