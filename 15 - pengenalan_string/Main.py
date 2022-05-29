# 15 - Pengenalan String

data = "Ini adalah String (Kumpulan karakter)"
print(data)
print(type(data))

# 1. Cara Membuat string
'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
    3. menggunakan keduanya langsung utk percakapan '"..."' atau "'...'"
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Ini adalah hari Jum'at")

# 2. Menggunakan tanda (\)
# Membuat tanda ' menjadi string
print('Mari Shalat Jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("c:\\user\\dzoelfikar")

# tab
print("ucup\t\t\totong, semakin jauh")

# backspace
print("ucup \botong, jadi deketan")

# enter/ new line
print("baris pertama.\nbaris kedua")  # LF -> Line feed -> unix, macos, linux
# CR -> Carriage return -> commodore, acorn, lisp
print("baris pertama.\rbaris kedua.")
# CRLF -> Line feed carriage return -> windows
print("baris pertama.\r\nbaris kedua.")

# 3. String Literal atau raw

# hati-hati
print('C:\new folder')  # akan salah pathya

# menggunakan raw string
print(r'c:\new folder')
print(r'c:\new folder')

# Multiline literal string
print("""
Nama: Ucup
Kelas: 5 SD
""")

# Multiline literal string dan RAW
print(r"""
Nama: Ucup
Kelas: 5 SD\new normal
Website: www.ucup.com/newId
""")
