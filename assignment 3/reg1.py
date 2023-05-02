# Write a regular expression that matches a date in the format dd/mm/yyyy.
# For example, the string "01/01/2021" should match.

import re


def validate_date(date_pattern, date_str):
    match = re.match(date_pattern, date_str)
    if match:
        print(date_str, "=>", "Valid date:", match.group())
    else:
        print(date_str, "=>", "Invalid date")
    return match


date_pattern = "(0[1-9]|[12][0-9]|3[01])\\/(0[1-9]|1[0-2])\\/([0-9]{4})"

# Validate date
print("\nValidate date:")

date_str = "24/04/2023"
validate_date(date_pattern, date_str)

date_str = "35/04/2023"
validate_date(date_pattern, date_str)

date_str = "xx/04/2023"
validate_date(date_pattern, date_str)

date_str = "24/14/2023"
validate_date(date_pattern, date_str)

# Extract dates from a string
print("\nExtract dates:")

text = "I'm on vacation from 11/02/2023 till 20/02/2023"
print(text)
dates = re.findall(date_pattern, text)
print(dates)
for d in dates:
    print("/".join(d))
