#Multiple Condition
country = input ("country:")

age = int(input("Enter Age:"))
if country == "USA" or age >=20:
  print("Allowed")
elif country == "UK" and age >=25:
  print("allowed")
else:
  print("Not Allowed")
