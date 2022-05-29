# 33 - Nested List (List di dalam List)

data_0 = [1, 2]
data_1 = [3, 4, 5]

data_list_biasa = [1, 2, 3, 4]
print(f"list biasa -> {data_list_biasa}")

list_2D = [data_0, data_1, data_list_biasa, 6]
print(f"ini adalah list 2D -> {list_2D}")

# contoh penggunaan
peserta_0 = ["Ucup", 25, "Laki-laki"]
peserta_1 = ["Otong", 10, "Laki-laki"]
peserta_2 = ["Odah", 50, "Perempuan"]

print(f"Peserta 0 -> {peserta_0}")
print(f"Peserta 1 -> {peserta_1}")
print(f"Peserta 2 -> {peserta_2}")

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"\nList Peserta -> \n{list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")

# Permasalahan dengan reference
list_copy = list_peserta.copy()
peserta_0[0] = "Michael"
print(f"List Peserta -> \n{list_peserta}")
print(f"List copy -> \n{list_copy}")

