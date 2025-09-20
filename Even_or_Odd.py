#check whether a number is even or odd

#Take input from the user
number = int(input("Enter a number: "))

#Check using if-else
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")
