text = 'Welcome to Iran'

# output = {
#     'a': 3,
#     'b': 10,
# }

result = dict()

for ch in text:
    t = result.get(ch)
    if t is None:
        result[ch] = 1
    else:
        result[ch] += 1

print(result)
