import re

regex = r'\d{8}@uttarauniversity\.edu\.bd'

email1 = 'abc123@uttarauniversity.edu.bd'  # invalid: contains letters and less than 8 digits
email2 = '22103030@uttarauniversity.edu.bd' # valid: 8-digit roll number and correct domain

print(f"'{email1}' matches: {bool(re.match(regex, email1))}")
print(f"'{email2}' matches: {bool(re.match(regex, email2))}")
