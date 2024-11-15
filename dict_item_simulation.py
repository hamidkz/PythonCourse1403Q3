my_dict = {
    "first_name": "Hamid",
    "last_name": "Kazemzadeh",
    "age": 43
}

print(list(my_dict.items()))
result = []
for key in my_dict.keys():
    result.append(
        (key, my_dict.get(key))
    )
print(result)

