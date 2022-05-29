# 40 - Looping Dictionary

teman_teman = {
    "cup": "Ucup surucup",
    "tong": "Otong surotong",
    "dung": "Dudung durudung",
    "sep": "Asep si kasyep",
    "cuy": "Ucuy surucuy"
}

# Looping dengan for
for teman in teman_teman:
    print(teman)  # yg muncul cuman key-nya saja

# operator utk mengambil item/iterables
keys = teman_teman.keys()
print("\n")
print(keys)

print("\n")
for key in teman_teman.keys():
    print(teman_teman.get(key))

print("\n")
values = teman_teman.values()
print(values)

print("\n")
for value in teman_teman.values():
    print(value)

print("\n")
# mengambil key dan value secara langsung
items = teman_teman.items()
print(items)

print("\n")
for item in teman_teman.items():
    print(item)

print("\n")
for key, value in teman_teman.items():
    print(f"key = {key}, value -> {value}")
