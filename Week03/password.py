import random
alphabets = 'abcdefgh'
lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
numbers = ['1', '2', '3', '4', '5'] 
special_chars = ['@', '!', '%', '$']

# 12 : 2 sp, 3 number, 4 low, 3 upp

my_password = []
for i in range(2):
    char = random.choice(special_chars)
    my_password.append(char)

for i in range(3):
    char = random.choice(numbers)
    my_password.append(char)

for i in range(4):
    char = random.choice(lower_chars)
    my_password.append(char)

for i in range(3):
    char = random.choice(lower_chars)
    my_password.append(char.upper())

random.shuffle(my_password)
print(my_password)

