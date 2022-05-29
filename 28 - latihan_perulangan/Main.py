# 28 - Latihan Perulangan (loops)

sisi = 10

# 1. Menggunakan for
# dummy variable
print("Awal for")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print("Akhir for")

print("\nAwal while")
# 2. Menggunakan while
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir while")

# 3. Hanya ganjil saja
print("\nAwal while")
count = 1
while True:
    if count % 2:
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika genap
        count += 1
        continue

    # akan break, jika count > sisi
    if count > sisi:
        break

print("Akhir while")


# 4. Hanya ganjil saja
print("\nAwal while")
count = 1
spasi = int(sisi / 2)
while True:
    if count % 2:
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break

print("Akhir while")
