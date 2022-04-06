from collections import Counter

word = input()
result = Counter(word)

for key, value in result.items():
    if key != ' ':
        print(f'{key} -> {value}')