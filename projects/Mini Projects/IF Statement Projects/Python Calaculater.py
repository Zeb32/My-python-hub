
# Simple Calculator in Python # This program performs basic arithmetic operations 

Operator = input("Enter the operator (+, -, *, /): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if Operator == "+":
    result = num1 + num2
    print("Result:", round(result,2))  
elif Operator == "-":
    result = num1 - num2
    print("Result:", round(result,2)) 
elif Operator == "*":
    result = num1 * num2
    print("Result:", round(result,2)) 
elif Operator == "/":
    result = num1 / num2
    print("Result:", round(result,2)) 
else:
    print("Invalid operator. Please enter one of +, -, *, /.") 
