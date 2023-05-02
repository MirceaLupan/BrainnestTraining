# Write a regular expression that matches a valid email address.
# For example, the string "example@example.com" should match.

import re


def validate_email(email_pattern, email_str):
    match = re.match(email_pattern, email_str)
    if match:
        print(email_str, "=>", "Valid email:", match.group())
    else:
        print(email_str, "=>", "Invalid email")
    return match


email_pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

# Validate email
print("\nValidate email:")

email_str = "example@example.com"
validate_email(email_pattern, email_str)

email_str = "name.surname@abc.xyz"
validate_email(email_pattern, email_str)

email_str = "name_surname_123@abc.xy"
validate_email(email_pattern, email_str)

email_str = "name/surname@abc/xyz"
validate_email(email_pattern, email_str)
