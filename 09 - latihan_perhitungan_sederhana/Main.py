# Latihan Konversi Satuan Temperature

# Program Konversi Celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan Suhu dalam Celcius: '))
print("Suhu adalah ", celcius)


# Reamur: (4/5) * C
reamur = (4/5) * celcius
print("Suhu dalam Reamur adalah: ", reamur)


# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah: ", fahrenheit)


# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah: ", kelvin)
