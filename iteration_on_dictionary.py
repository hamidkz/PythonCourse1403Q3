my_dict = {
    "first_name": "Hamid",
    "last_name": "Kazemzadeh",
    "age": 43
}

for key in my_dict.keys():
    value = my_dict[key]


for key, value in my_dict.items():
    print(key, value)