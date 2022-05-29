# 17 - Operasi dan Manipulasi String Part 2
# Operator dalam bentuk methods

# Merubah case dari string


salam = "bro!"
print("Normal: "+salam)

# merubah semua char ke upper case
salam = salam.upper()
print("Upper case: "+salam)

# merubah semua char ke lower case
alay = "aQu KeCE AbiiiesSZZzzZZZ"
print("Normal: " + alay)
alay = alay.lower()
print("Lower case: "+alay)

# pengecekkan dengan isX method
salam = "sist"
apakahLower = salam.islower()
print(salam + " is lower? " + str(apakahLower))

apakahUpper = salam.isupper()
print(salam + " is upper? " + str(apakahUpper))

# isalpha() <-- utk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isspace() <-- spasi, tab, newline

# istitle() <-- semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))  # jika salah satu kecil -> false


# Cek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = "+str(cek_end))

# Penggabungan/memisahkan komponen join() split <--
pisah = ['aku', 'sayang', 'kamu']

gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))


# Alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20, ":")
print("'"+tengah+"'")

# kebalikkannya -> strip()
tengah = tengah.strip(":")  # menghilangkan tanda (:)
print("'"+tengah+"'")
