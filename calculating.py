#Task 1: Sum of all numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i

print("Sum of all numbers from 1 to 50 is:", total)

#Task 2:Celsius to Fahrenheit Conversion Function
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example call
celsius_value = 37
result = convert_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C is equal to {result}°F")
