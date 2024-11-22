SALON = {
    'row_1': {
        'seat_1': 'Ali',
        'seat_2': 'Zahra',
        'seat_3': None
    },
    'row_2': {
        'seat_1': 'Mina',
        'seat_2': None,
        'seat_3': None
    },
    'row_3': {
        'seat_1': 'Hamid',
        'seat_2': None,
        'seat_3': None
    }
}

def reserve(name: str):
    for row in SALON.keys():
        for k, v in SALON[row].items():
            if v is None:
                SALON[row][k] = name
                return name, row, k

print(reserve('Reza'))
print(reserve('Mohsen'))