# Operasi Komparasi

# Setiap hasil dari operasi adalah bernilai Boolean (TRUE/FALSE)
a = 4
b = 2

# Lebih besar dari '>'
print("=== Lebih Besar dari ====")
result = a > 3
print(a, '>', 3, '=', result)
result = b > 3
print(b, '>', 3, '=', result)


# Kurang dari dari '<'
print("=== Kurang dari dari ====")
result = a < 3
print(a, '<', 3, '=', result)
result = b < 3
print(b, '<', 3, '=', result)


# Lebih besar dari atau sama dengan '>='
print("=== Lebih Besar dari atau sama dengan ====")
result = a >= 3
print(a, '>=', 3, '=', result)
result = b >= 3
print(b, '>=', 3, '=', result)


# Kurang dari atau sama dengan '<='
print("=== Kurang dari atau sama dengan ====")
result = a <= 3
print(a, '<=', 3, '=', result)
result = b <= 3
print(b, '<=', 3, '=', result)


# Sama dengan '=='
print("=== Sama dengan ====")
result = a == 4
print(a, '==', 4, '=', result)
result = b == 3
print(b, '==', 3, '=', result)


# Tidak sama dengan '!='
print("=== Sama dengan ====")
result = a != 4
print(a, '!=', 4, '=', result)
result = b != 3
print(b, '!=', 3, '=', result)


# 'is' -> komparasi utk membandingkan memory/object identity
x = 5  # ini adalah assignment membuat object
print("Object Identity 'is'")
y = 5
print('Nilai x = ', x, ' id = ', hex(id(x)))
print('Nilai y = ', y, ' id = ', hex(id(y)))

hasil = x is y
# hasil = x is 5  # 5 adalah literal/bukan object/variable
print(hasil)


# 'is not' -> komparasi utk membandingkan memory/object identity -> kebalikkan dari is
print("Object Identity 'is not'")
x = 5  # ini adalah assignment membuat object
y = 6
print('Nilai x = ', x, ' id = ', hex(id(x)))
print('Nilai y = ', y, ' id = ', hex(id(y)))

hasil = x is not y
# hasil = x is 5  # 5 adalah literal/bukan object/variable
print(hasil)
