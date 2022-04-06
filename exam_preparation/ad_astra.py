import re

info = input()
pattern = '\#([a-z A-Z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|' \
          '\|([a-z A-Z]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'
result = re.findall(pattern, info)
items = []
calories = 0

for item in result:
    current_item = [el for el in item if el != '']
    items.append(current_item)
    calories += int(current_item[2])

number_of_days = int(calories / 2000)

print(f'You have food to last you for: {number_of_days} days!')

for data in items:
    product = data[0]
    date = data[1]
    current_calories = data[2]
    print(f'Item: {product}, Best before: {date}, Nutrition: {current_calories}')

