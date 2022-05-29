# Operasi logika atau boolean -> and, or, not, xor

print('NOT')
a = False
c = not a
print('Data a =', a)
print('Data c =', c)

# OR -> Jika salah satu dari 2 buah nilai = True, maka hasil True
print('\nOR')
a = False
print('Data a =', a)
b = True
print('Data b =', b)
c = a or b
print('a', 'OR', b, '=', c)


# AND -> Hasil akan True, jika kedua buah nilai bernilai True
print('\nAND')
a = True
print('data a =', a)
b = True
print('data b =', b)
c = a and b
print(a, 'AND', b, '=', c)

# XOR -> Hasil akan True, jika salah satu True, dan jika keduanya True akan False
print('\nXOR')
a = False
b = False
print(a, 'XOR', b, '=', c)
a = False
b = True
print(a, 'XOR', b, '=', c)
a = True
b = False
print(a, 'XOR', b, '=', c)
a = True
b = True
print(a, 'XOR', b, '=', c)
