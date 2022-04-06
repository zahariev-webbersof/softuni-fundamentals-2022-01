import re

number_of_iterations = int(input())

for _ in range(number_of_iterations):
    data = input()
    pattern = '(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'
    result = re.match(pattern, data)

    if result is None:
        print("Invalid barcode")
    else:
        extract_nums = re.findall(r'\d', result.group())

        if not extract_nums:
            print(f'Product group: 00')
        else:
            print(f"Product group: {''.join(extract_nums)}")