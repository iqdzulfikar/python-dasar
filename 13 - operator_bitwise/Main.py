# 13 - Operator Bitwise, Biner, Binary


a = 9
b = 5

# Bitwise OR (|)
c = a | b
print(12*'=', 'OR', 13*'=', '\n')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))
print(12*'-', '(|)', 12*'-', '\n')
print('Nilai:', c, ', Binary:', format(c, '08b'))


# Bitwise AND (&)
c = a & b
print('\n')
print(12*'=', 'AND', 13*'=', '\n')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))
print(12*'-', '(&)', 12*'-', '\n')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n')
print(12*'=', 'XOR', 13*'=', '\n')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))
print(12*'-', '(^)', 12*'-', '\n')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print('\n')
print(12*'=', 'XOR', 13*'=', '\n')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print(12*'-', '(~)', 12*'-', '\n')
print('Nilai:', c, ', Binary:', format(c, '08b'))
print(12*'-', '(^)', 12*'-', '\n')
d = 0b0000001001
e = 0b1111111111
print('nilai:', e ^ d, ',  Binary:', format(e ^ d, '08b'))
