# 32 - Copy List (Teknik Menduplikat List)

a = ["Ucup", "Otong", "Dudung"]
print(f"a -> {a}")

b = a # pass by references
print(f"b -> {b}")

# merubah member dari list a
## keduanya akan berubah, meskipun kita maksudnya hanya ingin mengubah index ke-1 pada list a
a[1] = "Michael"  # [1] = Otong -> Michael
b.sort()
print(f"a -> {a}")
print(f"b -> {b}")

# print address dari kedua list utk mengetahui apakah keduanya = or ~
## kedua address ini bernilai sama
print(f"Address list a = {hex(id(a))}")
print(f"Address list b = {hex(id(b))}")

# Menduplikat list dengan copy()
print("Membuat list c dengan copy() methods")
c = a.copy() # full duplicate -> akan menjadi data baru (referencesnya juga berubah)

print(f"Address list a = {hex(id(a))}")
print(f"Address list b = {hex(id(b))}")
print(f"Address list c = {hex(id(c))}")

print("\nData awal sebelum diubah:")
print(f"a -> {a}")
print(f"b -> {b}")
print(f"c -> {c}")

print("\nKita ubah list c data 0")
c[0] = "Dadang"  # [0] = Ucup -> Dadang

print(f"a -> {a}")
print(f"b -> {b}")
print(f"c -> {c}")

print("\nKita ubah list a data 1")
a[1] = "Otong"

print(f"a -> {a}")
print(f"b -> {b}")
print(f"c -> {c}")
