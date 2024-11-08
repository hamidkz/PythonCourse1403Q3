lst = [ 2, 5, -1, 8, 1] # ... a, []
# output: -1

# min([ 2, 5, -1, 8, 1]) = min(2, min([5, -1, 8, 1]))
# min(lst) = min(lst[0], minimum(lst[1:]))

def minimum(a,b):
    return a if a<b else b

def find_min(lst):
    if lst == []:
        return None # int()
    else:
        k = find_min(lst[1:])
        return min(lst[0], find_min(lst[1:])) if k is not None else lst[0]

print(find_min(lst))

[2, 0, 5]
# find_min([2, 0, 5]): min(2, find_min([0, 5]))
# find_min([0, 5]): min(0, find_min([5]))
# find_min([5]): min(5, find_min([])) = min(5, None)
# find_min([]): None