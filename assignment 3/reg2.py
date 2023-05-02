# Write a regular expression that matches a phone number in the format xxx-xxx-xxxx,
# where x is a digit. For example, the string "123-456-7890" should match.

import re


def validate_number(number_pattern, number_str):
    match = re.match(number_pattern, number_str)
    if match:
        print(number_str, "=>", "Valid phone number:", match.group())
    else:
        print(number_str, "=>", "Invalid phone number")
    return match


number_pattern = "(\d{3})-(\d{3})-(\d{4})"

# Validate phone number
print("\nValidate phone number:")

number_str = "123-456-7890"
validate_number(number_pattern, number_str)

number_str = "1231-456-7890"
validate_number(number_pattern, number_str)

number_str = "123.456.7890"
validate_number(number_pattern, number_str)

# Extract phone numbers from a string
print("\nExtract phone numbers:")

text = "You can contact us on 123-456-7890, 234-567-8901, or 345-678-9012"
print(text)
number_pattern = "(\d{3})-(\d{3})-(\d{4})"
numbers = re.findall(number_pattern, text)
# print(numbers)
for d in numbers:
    print("-".join(d))
