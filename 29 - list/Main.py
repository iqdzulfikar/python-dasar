# 29 - List

# Kumpulan data numbers
data_angka = [1, 2, 5, 7, 3]
print(data_angka)
# Kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)
# Kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, "Gehu", 2, "Bakwan", "Ucup", True, "Otong", False]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10)
print(list(data_range))

data_range = range(0, 10, 2)  # range (start, stop, step)
print(list(data_range))

# membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0, 10)]
print(list_pake_for)

list_pake_for = [i**3 for i in range(0, 10)]  # di kuadratin dulu si i nya
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(1, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(1, 10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(1, 10) if i % 2 != 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(1, 10) if i % 2 != 0]
print(list_pake_for_if)
