lst = [1, 2, 3, 4, 5, 6] # (k: 1) -> [6, 1, 2, 3, 4, 5] 
k = 3
for i in range(k):
    last_member = lst.pop(len(lst)-1)
    lst.insert(0, last_member)
print(lst)