# Write a regular expression that matches a string that contains a number
# with exactly two decimal places. For example, the string "1.23" should match,
# but the string "1.234" should not match.

import re


def validate_number(number_pattern, number_str):
    match = re.match(number_pattern, number_str)
    if match:
        print(number_str, "=>", "Valid number:", match.group())
    else:
        print(number_str, "=>", "Invalid number")
    return match


number_pattern = "(\d+\.\d\d)(?!\d)"

# Validate number
print("\nValidate number:")

number_str = "1.23"
validate_number(number_pattern, number_str)

number_str = "101.23"
validate_number(number_pattern, number_str)

number_str = "1.234"
validate_number(number_pattern, number_str)

number_str = "123.4"
validate_number(number_pattern, number_str)

# Extract numbers of given format from a string
print("\nExtract numbers:")
text = "1.23 abc 456.78 0 5.2"
print(text)
numbers = re.findall(number_pattern, text)
print(numbers)
