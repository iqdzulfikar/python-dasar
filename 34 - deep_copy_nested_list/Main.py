# 34 - Deep Copy Nested List

data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy()  # duplicate nested list
print(f"Data 2D -> {data_2D}")
print(f"Data 2D Copy-> {data_2D_copy}")

# Mengambil data dari nested list
data = data_2D[1][0]
print(data)

# mengambil address list
print(f"Address Data 2D -> {hex(id(data_2D))}")
print(f"Address Data 2D Copy -> {hex(id(data_2D_copy))}")

## address member akan sama -> kecuali jika member bukan merupakan list
print(f"\nAddress Member ke-1")
print(f"Address Data 2D -> {hex(id(data_2D[0]))}")
print(f"Address Data 2D Copy -> {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[2] = 9
print(f"\nData 2D -> {data_2D}")
print(f"Data 2D Copy -> {data_2D_copy}")

# menggunakan deep copy
from copy import deepcopy

data_2D = [data_0, data_1,10]
data_2D_deepcopy = deepcopy(data_2D)
print(f"\n\nAddress Asli -> {hex(id(data_2D))}")
print(f"Address Deepcopy -> {hex(id(data_2D_deepcopy))}")

print(f"\n\nAddress Member ke-1")
print(f"Address Data 2D -> {hex(id(data_2D[0]))}")
print(f"Address Data 2D Copy -> {hex(id(data_2D_deepcopy[0]))}")


data_2D[1][0] = 30
print(f"\nData 2D -> {data_2D}")
print(f"Data 2D Copy -> {data_2D_copy}")
print(f"Data 2D Deepcopy -> {data_2D_deepcopy}")

