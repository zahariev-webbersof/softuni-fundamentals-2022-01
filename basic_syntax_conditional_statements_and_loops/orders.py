number_of_orders = int(input())
total_sum = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    price_for_current_order = days * capsules_count * price_per_capsule
    total_sum += price_for_current_order
    print(f'The price for the coffee is: ${price_for_current_order:.2f}')

print(f'Total: ${total_sum:.2f}')
