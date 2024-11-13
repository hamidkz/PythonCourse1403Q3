text = 'iran08tehran349' # ['08', '349'] 
n = ''
result = []
for ch in text:
    if ch.isdigit(): # 9
        n += ch # n = '349'
    else:
        result.append(n)
        n = ''
else:
    result.append(n)
new_result = [item for item in result if item != '']
print(new_result)

