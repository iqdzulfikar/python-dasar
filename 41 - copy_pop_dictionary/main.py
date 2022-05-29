# 41 - Copy and Pop Dictionary

teman_teman = {

    "cup": "Ucup surucup",
    "tong": "Otong surotong",
    "dung": "Dudung durudung",
    "sep": "Asep si kasyep",
    "cuy": "Ucuy surucuy"
}
# menduplicate dictionary copy()
friends = teman_teman.copy()

print(f"teman-teman -> \n{teman_teman}")
print(f"Friends -> \n{friends}")

teman_teman["cup"] = "Ucup si kweren"

print(f"teman-teman -> \n{teman_teman}")
print(f"Friends -> \n{friends}")

# pop dictionary -> mentransfer item berdasarkan key dict
data_asep = friends.pop("sep")
print(f"data asep: {data_asep}")
print(f"friends: {friends}")

# pop item dictionary -> mentransfer item terakhir pada dict
data_terakhir = friends.popitem()
print(f"data_terakhir (items) yang diambil: {data_terakhir}")
print(f"friends: {friends}")
