class Party:
    def __init__(self):
        self.people = []

party = Party()
obj = Party()
while True:
    command = input()

    if command == 'End':
        break
    party.people.append(command)

# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

print(party.people)
print(obj.people)