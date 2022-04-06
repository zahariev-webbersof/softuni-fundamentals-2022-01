def miner_task():
    items_dict = {}

    while True:
        resource = input()

        if resource == 'stop':
            break

        quantity = int(input())

        if resource not in items_dict:
            items_dict[resource] = quantity
        else:
            items_dict[resource] += quantity

    for key, value in items_dict.items():
        print(f'{key} -> {value}')

miner_task()
