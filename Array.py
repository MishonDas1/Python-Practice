num1 = [10, 11, 12, 13, 14]
num2 = [15, 16, 17, 18, 19]

for i in range(len(num1)):
    if i % 2 == 0:
        print("Even index number in num1 is", num1[i])
    else:
        print("Odd index number in num1 is", num1[i])

for i in range(len(num2)):
    if i % 2 == 0:
        print("Odd index number in num2 is", num2[i])
    else:
        print("Even index number in num2 is", num2[i])
