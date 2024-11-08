import random

colors = ['R', 'G', 'B']
random.shuffle(colors)
for i in range(3):
    user_choices = input("Enter your choices: ") # r b g
    user_choices_lst = user_choices.split(' ') # ['r', 'b', 'g']
    result = []
    for idx in range(len(colors)):
        result.append(colors[idx].lower() == user_choices_lst[idx].lower())

    if result == [True, True, True]:
        print("Hooooraaa!!!!")
        break
    print(result)    



