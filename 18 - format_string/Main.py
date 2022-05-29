# 17 - Format String

# contoh generic


nama = "ucup"
formatStr = f"hello {nama}"
print(formatStr)

# angka
angka = 2005.5
formatStr = f"angka = {angka}"
print(formatStr, type(angka))

# bilangan bulat
angka = 15
formatStr = f"bilangan bulat = {angka:d}"
print(formatStr)

# bilangan dengan ordo ribuan
angka = 3000
formatStr = f"Ribuan = {angka:,}"
print(formatStr)

angka = 3000000
formatStr = f"Jutaan = {angka:,}"
print(formatStr)

# boolean
boolean = True
formatStr = f"boolean = {boolean}"
print(formatStr)

# bilangan desimal
angka = 2005.54321
formatStr = f"Desimal = {angka:.3f}"
print(formatStr)

# menampilkan leading zero
angka = 2005.54321
formatStr = f"Desimal = {angka:010.3f}"
print(formatStr)

# menampilkan tanda + atau -
minus = -10
plus = 10.2
format_minus = f"minus = {minus:+d}"
format_plus = f"plus = {plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp. {harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
