# 37 - Tuples and Sets

## List
# menggunakan kurung siku []
data_list = [10, 2, 4, 3, 2]

## Tuples -> Collection yang di dalamnya tidak bisa dirubah (immutable/final)
# menggunakan ()
data_tuples = (7, 8, 9, 10)
# data_tuples[1] = "Ucup" # ERROR -> Tidak bisa dilakukan di dalam tuples
# data_tuples.append(1) # ERROR -> Tidak bisa dirubah

## Sets -> Collection yang tidak memiliki index (Himpunan)
# menggunakan kurang kurawal {}
data_sets = {10, 4, 3, 2, 4, 7, 6, 5}
# print(data_sets[0]) # ERROR <- Tidak bisa dilakukan indexing