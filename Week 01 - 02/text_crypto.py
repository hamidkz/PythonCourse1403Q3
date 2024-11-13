mapping = [
    ['a', 'x'],
    ['i', 'h'],
    ['r', 't'],
    ['n', 'w'],
    ['q', 'p'],
    ['m', 'a'],
]

orginal_txt = 'iran'
orginal_list = []
result = ''
for ch in orginal_txt:
    orginal_list.append(ch)
# orginal_list = ['i', 'r', 'a', 'n']
for item in orginal_list:
    # item : 'i'
    for m in mapping:
        if m[0] == item:
            result += m[1]
print(result)


