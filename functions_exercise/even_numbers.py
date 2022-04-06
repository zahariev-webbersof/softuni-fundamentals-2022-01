result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
print(result)


def check_even(number):
    if number % 2 == 0:
        return True

    return False

result = filter(check_even, list(map(int, input().split(' '))))
print(list(result))