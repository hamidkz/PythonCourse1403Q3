def sum(*args):
    result = 0
    for num in args:
        result += num
    return result 

# print(sum(3, 5, 8, 10))

# my_dict = {}
# my_dict.update(name='hamid', age=43, company='sg')
# print(my_dict)

# my_dict = dict()
# def update_dictionary(name, age):
#     my_dict['name'] = name
#     my_dict['age'] = age

# print(my_dict)
# update_dictionary(name='hamid', age=43)
# print(my_dict)

my_dict = dict()
def update_dictionary(*args, **kwargs):
    # print(kwargs)
    my_dict.update(kwargs)

update_dictionary(name='hamid', age=43, company='sg')
print(my_dict)