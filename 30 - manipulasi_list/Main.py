# 30 - Manipulasi List

# index   0(-3)    1(-2)  2(-1)
data = ["otong", "ucup", "odah"]
# mengambil data dari list
data_0 = data[0]  # mengambil data pertama
print(f"Data pertama (index 0) -> {data_0}")

data_terakhir = data[-1]  # mengambil data terakhir
print(f"Data terakhir -> {data_terakhir}")

# mengetahui info panjang list
panjang_data = len(data)
print(f"panjang data -> {panjang_data}")

## Memanipulasi data list
# menambahkan item ke dalam list
print(f"data sebelum ditambahkan\n {data}")
data.insert(1, "Asep")  # --> menambahkan item 'Asep' ke dalam index 1
print(f"data sesudah ditambah \n{data}")

# menambah item di akhir list
data.append("Jajang")
print(f"data sesudah ditambah lagi \n{data}")

# menambah list dengan list lagi
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita merubah item 2 (ucup) menjadi michael
data[2] = "Michael"
print(f"data rubah = \n{data}")
print(f"panjang data -> {len(data)}")

# meremove data
data.remove("Ujang")
print(f"data remove \n{data}")
print(f"panjang data -> {len(data)}")
# data.remove("usep") # ERROR -> karena case sensitive (usep)

# meremove data paling belakang/ akhir
data_akhir = data.pop()
print(f"data akhir = \n{data}")
print(data_akhir)
