students = [
    [16, 17, 12, 19],
    [12, 14, 20, 20],
    [18, 18, 18, 18],
]


result = map(lambda scores: sum(scores)/len(scores), students)
print(list(result))
