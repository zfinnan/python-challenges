# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def calculate():
    def add(num1, num2): 
        return num1 + num2 
    def subtract(num1, num2): 
        return num1 - num2 
    def multiply(num1, num2): 
        return num1 * num2 
    def divide(num1, num2): 
        return num1 / num2 
    calculation = input('What calculation would you like to do? (add, subtract, multiply, divide)')
    number_1 = int(input("What is the first number: ")) 
    number_2 = int(input("What is the second number: ")) 
    if calculation == 'add': 
        print(number_1, "+", number_2, "=", 
                        add(number_1, number_2)) 
    elif calculation == 'subtract': 
        print(number_1, "-", number_2, "=", 
                        subtract(number_1, number_2)) 
    elif calculation == 'multiply': 
        print(number_1, "*", number_2, "=", 
                        multiply(number_1, number_2)) 
    elif calculation == 'divide': 
        print(number_1, "/", number_2, "=", 
                        divide(number_1, number_2)) 
    else: 
        print("Invalid input")

print(calculate())