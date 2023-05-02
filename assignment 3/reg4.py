# Write a regular expression that matches a string that starts with a word,
# followed by one or more whitespace characters, followed by another word.
# For example, the string "hello world" should match.

import re


def validate_expression(pattern, expression):
    match = re.match(pattern, expression)
    if match:
        print(expression, "=>", "Valid expression:", match.group())
    else:
        print(expression, "=>", "Invalid expression")
    return match


pattern = "^[A-Za-z]+\s+[A-Za-z]+"

# Validate expression
print("\nValidate expression:")

expression = "hello world"
validate_expression(pattern, expression)

expression = "hello world!!!"
validate_expression(pattern, expression)

expression = "hello, world"
validate_expression(pattern, expression)

expression = "-hello world-"
validate_expression(pattern, expression)
