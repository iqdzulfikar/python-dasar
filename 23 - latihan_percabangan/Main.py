# 23 - Latihan percabangan

print(20*"=")
print("Calculator Sederhana")
print(20*"=")


angka_1 = float(input("Masukkan Angka 1: "))
operator = input("operator (+, -, x, /): ")
angka_2 = float(input("Masukkan Angka 2: "))


# percabangannya
if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/" or operator == ":":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("Masukkan yang benar dong! Aku pusying.")

print("Akhir dari program")
