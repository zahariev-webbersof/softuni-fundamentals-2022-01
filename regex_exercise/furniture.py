budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())
costs = 0

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05

costs = number_of_nights * price_per_night
additional_costs = budget * (percent_additional_costs / 100)
costs += additional_costs

diff = abs(budget - costs)

if budget >= costs:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')