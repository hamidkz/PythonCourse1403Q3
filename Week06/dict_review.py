my_dict = {
    "name": "hamid",
    "age": 43
}

# my_list = ["hamid", 43]

print(my_dict["name"])
# print(my_dict["company"])
print(my_dict.get("company", "Not found!"))
my_dict["company"] = 'SG'
print(my_dict.get("company", "Not found!"))

