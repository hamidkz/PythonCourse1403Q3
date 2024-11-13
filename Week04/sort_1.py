lst = ['Iran', 'Iraq', 'Arak', 'France', 'England', 'USA']

lst.sort(key=lambda c: [len(c), c])
# sorted_list = sorted(lst, key=lambda c: [len(c), c])
# print(sorted_list)
print(lst)