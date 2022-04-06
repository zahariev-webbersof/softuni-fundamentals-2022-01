events = input().split('|')
energy = 100
coins = 100
close_condition = False

for event in events:
    current_event_elements = event.split('-')
    command = current_event_elements[0]
    number = int(current_event_elements[1])

    if command == 'rest':
        if energy >= 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")

        print(f"Current energy: {energy}.")

    elif command == 'order':
        if energy >= 30:
            print(f"You earned {number} coins.")
            energy -= 30
            coins += number
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            print(f"You bought {command}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {command}.")
            close_condition = True
            break

if not close_condition:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")