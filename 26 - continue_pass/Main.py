# 26 - Continue and Pass

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# number = 0
# while number < 5:
#     number += 1

#     if number == 3:
#         pass # tidak akan dieksekusi

#     print(number)

# print("Akhir dari program.")


# continue --> meloncat ke step selanjutnya

number = 0

print(f"Angka sekarang --> {number}")

while number < 5:
    number += 1
    print(f"Angka sekarang --> {number}")  # aksi 1

    if number == 3:
        print("nice!")
        continue    # meloncat ke step loop selanjutnya

    print("Whassup!")  # aksi 2

print("Akhir program.")
