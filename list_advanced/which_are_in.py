substrings = input().split(', ')
sentence = input()
result = [el for el in substrings if el in sentence] # 'lively, alive, harp, sharp, armstrong'
print(result)