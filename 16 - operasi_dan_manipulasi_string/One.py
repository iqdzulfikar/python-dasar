# 16 - Operasi dan Manipulasi String Part 1

# 1. Menyambung string (contatenate)
firstName = "ucup"
middleName = "D"
lastName = "Fame"

fullName = firstName + " "+middleName + "'"+lastName
print(fullName)


# 2. Menghitung panjang string
panjang = len(fullName)
print("Panjang dari " + fullName + " = " + str(panjang))

# Operator untuk string

# Mengecek apakah ada komponen char atau string di string
d = "d"
status = d in fullName
print(d+" ada di " + fullName + " = "+str(status))

d = "D"
status = d in fullName
print(d+" ada di " + fullName + " = "+str(status))

d = "d"
status = d not in fullName
print(d+" tidak ada di " + fullName + " = "+str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing (mengambil data dari string/memotong)
print("index ke-0: " + fullName[0])  # mulai index di 0
print("index ke-5: " + fullName[5])  # mulai index di 0
print("index ke-(-1): " + fullName[-1])  # mengambil dari belakang
print("index ke-(-2): " + fullName[-2])  # mengambil dari belakang
print("index ke-[0:3]: " + fullName[0:4])
print("index ke-[3:7]: " + fullName[3:8])
# index 0:10 - setter_getter dengan jeda 2/increment 2
print("index ke-[0,2,4,6,8,10 - setter_getter]: " + fullName[0:10:2])

# item paling kecil
print("Paling kecil: "+min(fullName))

# item paling besar
print("Paling besar: " + max(fullName))

# mengambil ASCII Code
ascii_code = ord(" ")
print("ASCII Code untuk spasi adalah: " + str(ascii_code))

# ASCII Code ke String
data = 117
print("Char untuk ASCII 117 adalah "+chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah 'o' pada " + data + " = " + str(jumlah))
