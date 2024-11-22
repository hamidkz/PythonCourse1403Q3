f = open('Week06\my_text.txt', mode='a')
f.write('Hello2')
f.close()

with open('Week06\my_text.txt', mode='w') as f:
    f.writelines(['100', '\n', '200', '\t', '0444'])



