# 36 - Latihan List

list_buku = []

while True:
    print("\nMasukkan Data Buku")
    judul = input("Masukkan judul buku\t: ")
    penulis = input("Masukkan penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("=" * 20, "Data Buku", "=" * 20)
    for index, buku in enumerate(list_buku):
        print(f"| {index + 1} | {buku[0]} | {buku[1]}")


    print("=" * 40)
    isNext = input("Apakah ingin Dilanjutkan [y/n]? ")

    if isNext == "y":
        continue
    else :
        break

print("\n\nProgram selesai.")
