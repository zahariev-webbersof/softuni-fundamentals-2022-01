def orders_func(orders_dict, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product in orders_dict:
        orders_dict[product] = [price, (quantity + orders_dict[product][1])]
    else:
        orders_dict[product] = [price, quantity]

    return orders_dict

def orders():

    orders_dict = {}

    while True:
        command = input()

        if command == 'buy':
            break

        command = command.split(' ')
        orders_dict = orders_func(orders_dict, command)

    for k in orders_dict:
        total_sum = orders_dict[k][0] * orders_dict[k][1]
        print(f'{k} -> {total_sum:.2f}')

orders()