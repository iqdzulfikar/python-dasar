# 12 - Latihan Logika dan Komparasi

inputUser = float(input(
    "Masukkan Angka yang bernilai dari\nkurang dari 3\natau\nlebih besar dari 10 - setter_getter: "))

# Memeriksa angka yang kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 =', isKurangDari)


# Memeriksa angka yang lebih dari 10 - setter_getter
isLebihDari = (inputUser > 10)
print('Lebih besar dari 10 - setter_getter =', isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('Angka yang Anda masukkan:', isCorrect)


# IRISAN
print('\n', 10*'=', '\n')
inputUser = float(input(
    "Masukkan Angka yang bernilai dari\nkurang dari 3\ndan\nlebih besar dari 10 - setter_getter: "))
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 =', isLebihDari)

# kurang dari 10 - setter_getter
isKurangDari = inputUser < 10
print('Kurang dari 10 - setter_getter =', isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('Angka yang Anda masukkan:', isCorrect)
