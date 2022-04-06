import re

text = input()

user_pattern = r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'

host_pattern = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'

pattern = rf'{user_pattern}@{host_pattern}'

emails = re.finditer(pattern, text)

for email in emails:
    print(email[0])