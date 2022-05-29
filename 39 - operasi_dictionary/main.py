# 39 - Operasi di Dictionary

data_dict = {
    "cup": "Ucup surucup",
    "tong": "Otong surotong",
    "dung": "Dudung durudung"
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary -> {LENDICT}")

# cek key exist atau tidak
KEY = "cup"
CHECK_KEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict: {CHECK_KEY}")  # True

# mengakses value (read) dengan get()
print(data_dict["cup"])  # utk mengakses list
print(data_dict.get("cup"))  # utk mengakses dict
print(data_dict.get("kos"))  # menghasilkan 'none' (bukan error spt mengakses list)
print(data_dict.get("kos", "Key yang dimaksud tidak ditemukan"))  # menghasilkan message bukan none

# mengupdate data di dalam dictionary
data_dict["cup"] = "Ucup si guanteng"
print(data_dict)
data_dict["sep"] = "Asep si kasyep"  # bisa menambah data baru spt ini <-
print(data_dict)

## mengupdate dengan update()
data_dict.update({"cup": "Ucup surucup"}) # kalo key ada di dict, data yg ada hanya di update
print(data_dict)

# kalo key belum ada di dict, maka key dengan data yg dimasukkan ditambahkan
data_dict.update({"rifqi":"dzulfikar"})
print(data_dict)


# menghapus data/item pada dictionary
del data_dict["rifqi"]
print(data_dict)