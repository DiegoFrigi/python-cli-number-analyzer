num1 = float(input("Enter a number: "))
operator = input("Enter an operator(+, -, *, /): ")
num2 = float(input("Enter another number: "))

if num1 == 5:
    result = num1 + num2
    print(round(result, 3))
elif num1 == 6:
    result = num1 - num2
    print(round(result, 3))
elif num1 == 7:
    result = num1 * num2
    print(round(result, 3))
elif num1 == 8:
    result = num1 / num2
    print(round(result, 3))
else:
    print("You need to write an operator!")  

print("finished ")