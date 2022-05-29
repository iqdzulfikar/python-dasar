# Latihan Operasi Logika dan Komparasi

# Soal No.1: --0++5--8++11--
inputUser = float(input("Angka > 0 and < 5 or > 8 and < 11: "))

isLebihBesarDariNol = inputUser > 0
print(isLebihBesarDariNol)

isKurangDariLima = inputUser < 5
print(isKurangDariLima)

isLebihDariDelapan = inputUser > 8
print(isLebihDariDelapan)

isKurangDariSebelas = inputUser < 11
print(isKurangDariSebelas)

isCorrect = (isLebihBesarDariNol and isKurangDariLima) or (
    isLebihDariDelapan or isKurangDariSebelas)
print('Angka yang Anda masukkan: ', isCorrect)

# Soal No. 2: ++0--5++8--11++
print('\n', 10*'*', '\n')
inputUser = float(input("Angka < 0 or > 5 and < 8 or > 11: "))

isKurangDariNol = inputUser < 0
print(isKurangDariNol)

isLebihDariLima = inputUser > 5
print(isLebihDariLima)

isKurangDariDelapan = inputUser < 8
print(isKurangDariDelapan)

isLebihDariSebelas = inputUser > 11
print(isLebihDariSebelas)

isCorrect = (isKurangDariNol or isLebihDariLima) and (
    isKurangDariDelapan or isLebihDariSebelas)
print('Angka yang anda masukkan: ', isCorrect)
