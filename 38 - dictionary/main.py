# 38 - Dictionary

## List merupakan contoh Array di dalam python. Untuk mengaksesnya menggunakan index

data_list = ['Ucup', 'Otong', 'Dudung']
print(data_list[0])

# Dictionary (dict) -> Assosiative Array untuk mengaksesnya menggunakan key
## Identifier -> key

data_dict = {
    'key': 'value',
    'cp': 'ucup',
    'tg': 'otong',
    'dg': 'dudung',
    'num': 11,
    'list': data_list
}
print(data_dict['key'])
print(data_dict['tg'])
print(data_dict['num'])
print(data_dict['list'])
