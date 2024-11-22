text_1 = 'hello'
text_2 = 'My name is Hamid'
text_3 = 'my country is Iran'

# {
#     "hello": 1,
#     'my': 2,
#     ...
# }

words = []
for text in [text_1, text_2, text_3]:
    words.extend(text.split(' '))

# for idx, w in enumerate(words):
#     words[idx] = w.lower()

words = list(set([w.lower() for w in words]))

# print(words)

result = {}.fromkeys(words, 0)
# print(result)

def count_word_in_text(text: str, word: str):
    return text.lower().count(word.lower())

for key in result:
    count_in_text_1 = count_word_in_text(text_1, key)
    count_in_text_2 = count_word_in_text(text_2, key)
    count_in_text_3 = count_word_in_text(text_3, key)
    result[key] = count_in_text_1 + count_in_text_2 + count_in_text_3

# print(result)

filtered_result = {key: value for key, value in result.items() if value == 1}
print(filtered_result)
