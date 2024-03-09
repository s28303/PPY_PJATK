# Exercise 1.
# Ask 3 questions about the name, surname and age, and at the end create a sentence with this information.
name = input("Enter your first name: ")

surname = input("Enter your surname: ")

age = input("Enter your age: ")

print(f'Hello {name} {surname}. You are {age} years old!')


# Exercise 2.
# Reverse to change Fahrenheit to Celsius.
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) / (9/5)

print(f"Temperature in Celsius: ", celsius)


# Exercise 3.
# Convert to the Polish grading system.
# https://dsm.usz.edu.pl/grades/
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 85:
    grade = "4.5"
elif score >= 75:
    grade = "4"
elif score >= 70:
    grade = "3.5"
elif score >= 60:
    grade = "3"
else:
    grade = "2"

print("Your grade is:", grade)


# Exercise 4.
# Change the code so that there are two inputs and the first number it can be devidet.
number1 = int(input("Enther first number: "))
number2 = int(input("Enther second number: "))

if number1 % number2 == 0:
    print("First number can be devided by the second")
else:
    print("First number can't be devided by the second")


# Exercise 6.
# Add a check to see if a triangle can be drawn with the given sides.
# Triangle Inequality Theorem
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Triable is valid, so is drawable")
else:
    print("Trianle can't be drawn!")


# Exercise 7.
# Add a check to see if someone is trying to divide by zero, if so, give an appropriate message
    num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Devision by zero is not possible!"
else:
    result = "Invalid operation"

print("Result:", result)