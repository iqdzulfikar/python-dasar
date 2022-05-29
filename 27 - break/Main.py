# 27 - Break -> mengakhiri/keluar perulangan meskipun kondisi perulangan belum selesai

# Contoh 1
angka = 0

while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}")

    if angka == 3:
        print("Naise!")
        break

    print("Whasupp!")

print("Pinis!")


# Contoh 2
# data_int = int(input("Hitung sampai: "))
# angka = 0

# while True:
#     angka += 1
#     print(f"count = {angka}")
#     if angka == data_int:
#         print("Naise!")
#         break

#     print("Whasupp!")

# print("Pinis!")
