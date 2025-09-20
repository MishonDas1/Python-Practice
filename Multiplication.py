#Task 1: Multiplication Table
num = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Task 2:List of Favorite Fruits
# Step 1: Create list of 5 fruits
fruits = ["Mango", "Banana", "Apple", "Orange", "Grapes"]
print("\nInitial list of fruits:")
print(fruits)

#Step 2: Add one more fruit
fruits.append("Pineapple")
print("\nAfter adding one more fruit:")
print(fruits)

#Step 3: Remove the 3rd fruit (index 2)
removed_fruit = fruits.pop(2)
print(f"\nAfter removing the 3rd fruit ({removed_fruit}):")
print(fruits)
