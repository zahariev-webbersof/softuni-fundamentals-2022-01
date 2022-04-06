import re

regex = r"\d+"

while True:
    test_str = input()

    if not test_str:
        break

    matches = re.finditer(regex, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
          print(match[0], end=' ')