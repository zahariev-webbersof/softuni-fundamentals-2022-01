def extract_func(command, data_dict):
    command = command.split('||')
    town = command[0]
    population = int(command[1])
    gold = int(command[2])

    if town not in data_dict:
        data_dict[town] = [population, gold]
    else:
        data_dict[town][0] += population
        data_dict[town][1] += gold

    return data_dict

def sail_func(command, data_dict):
    command = command.split('=>')
    current_command = command[0]

    if current_command == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])

        data_dict[town][0] -= people
        data_dict[town][1] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if data_dict[town][0] <= 0 or data_dict[town][1] <= 0:
            del data_dict[town]
            print(f"{town} has been wiped off the map!")

    elif current_command == 'Prosper':
        town = command[1]
        gold = int(command[2])

        if gold > 0:
            data_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {data_dict[town][1]} gold.")
        else:
            print("Gold added cannot be a negative number!")

    return data_dict

def pirates():
    data_dict = {}
    condition = False
    while True:
        command = input()

        if command == 'End':
            break
        elif command != 'Sail' and not condition:
            data_dict = extract_func(command, data_dict)

        elif command == 'Sail':
            condition = True
            continue

        elif condition:
            data_dict = sail_func(command, data_dict)

    print(f'Ahoy, Captain! There are {len(data_dict)} wealthy settlements to go to:')

    for data in data_dict:
        town = data
        current_population = data_dict[data][0]
        current_gold = data_dict[data][1]
        print(f'{town} -> Population: {current_population} citizens, Gold: {current_gold} kg')

pirates()