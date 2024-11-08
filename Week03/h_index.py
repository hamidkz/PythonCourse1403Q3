articles = [3, 0, 10, 2, 4, 8]
# h-index: 3

h_index = len(articles) # 6
while h_index >= 0:
    if len([item for item in articles if item > h_index]) >= h_index: 
        break
    else:
        h_index = h_index - 1

print(h_index)
