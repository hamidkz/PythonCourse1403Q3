my_dict = {
"Ali": 35,
"Reza": 65,
"Zahra": 20,
"Hamid": 43,
"Mina": 70,
"Alex": 99
}
# a=list(my_dict.items())
# a.sort()
# print(a)
result_list = sorted(my_dict.items(), key=lambda item: item[1])
result = {key: value for key, value in result_list}
print(result)

