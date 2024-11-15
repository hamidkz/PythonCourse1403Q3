my_dict = {
    "Ali": 35,
    "Reza": 65,
    "Zahra": 20,
    "Hamid": 43,
    "Mina": 70,
    "Alex": 99 
}
#  > 60

# result = []
# for key, value in my_dict.items():
#     if value > 60:
#         result.append(key)
# print(result)

result = list(filter(lambda key_value_tuple: key_value_tuple[1] > 60, my_dict.items()))
print(result)

# lst = [1, 2, 3, 4, 5]
# result = [i**2 for i in lst if i > 3] List comprehention
result = {key: value for key, value in my_dict.items() if value > 60}
print(result)
