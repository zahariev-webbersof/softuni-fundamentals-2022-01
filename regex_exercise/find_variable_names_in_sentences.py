import re

regex = r"\b_[a-zA-Z0-9]+\b"

test_str = input()

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print(match[0][1:], )