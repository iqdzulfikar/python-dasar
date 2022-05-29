# 35 - Looping List dengan Loop dan Enummerate

## 1.Dengan Looping

## 1.1. Looping dengan for loop
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f"Angka -> {angka}")

print("\n")
peserta = ["Ucup", "Otong", "Dadang", "Diding", "Dudung"]
for nama in peserta:
    print(f"Nama -> {nama}")

## 1.2. Looping dengan for loop dan range
kumpulan_angka = [10, 5, 4, 22, 6, 5]
panjang = len(kumpulan_angka)
for index in range(panjang):
    print(f"angka = {kumpulan_angka[index]}")
## 1.3. While
print("\nWhile Loop")
kumpulan_angka = [10, 5, 4, 22, 6, 5]
panjang = len(kumpulan_angka)
index = 0
while index < panjang:
    print(f"angka = {kumpulan_angka[index]}")
    index += 1

## 2. Dengan List Comprehension
print("\nList Comprehension")
data = ["Ucup", 1, 2, 3, "Otong"]

[print(f"data = {i}") for i in data]

# membuat kuadrat langsung dari sebuah list
list_angka = [10, 5, 4, 22, 6, 5]
angka_kuadrat = [i ** 2 for i in list_angka]
print(f"List Angka -> {list_angka}")
print(f"List Angka kuadrat -> {angka_kuadrat}")

## 3. Dengan Enumerate
print("\n\nEnumerate")
data_list = ["Ucup", 1, 2, 3, "Otong"]

for index, data in enumerate(data_list):  # menampilkan index dan data sekaligus
    print(f"index ke-({index}), data = {data}")
