num1 = int(input())
num2 = int(input())
new_list = []

for num in range(1, num2 + 1):
    new_list.append(num * num1)

print(new_list)