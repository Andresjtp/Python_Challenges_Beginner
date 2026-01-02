class Calculator:

    @staticmethod
    def add(num1, num2):
        result = num1 + num2
        return result
    
    @staticmethod
    def subtract(num1, num2):
        result = num1 - num2
        return result

    @staticmethod
    def multiply(num1, num2):
        result = num1 * num2
        return result

    @staticmethod
    def divide(num1, num2):
        result = num1 / num2
        return result 

while True:
    try:
        first_input = input("Enter a number: ")
        if not first_input:
            raise ValueError("Please enter a number.")
        first_input = int(first_input)
        
        operator = input("enter operator: ")

        second_input = input("Enter a number: ")
        if not second_input:
            raise ValueError("Please enter a number: ")
        if operator == "/" and int(second_input) == 0:
            raise ZeroDivisionError("You can't divide by zero ")
        second_input = int(second_input)

        if operator == "+":
            print(f"{first_input} {operator} {second_input} = ", Calculator.add(first_input, second_input))
        elif operator == "-":
            print(f"{first_input} {operator} {second_input} = ", Calculator.subtract(first_input, second_input))
        elif operator == "*":
            print(f"{first_input} {operator} {second_input} = ", Calculator.multiply(first_input, second_input))
        elif operator == "/":
            print(f"{first_input} {operator} {second_input} = ", Calculator.divide(first_input, second_input))
        else:
            raise ValueError("Please enter either +, -, *, or /")
        break

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except ZeroDivisionError as zde:
        print(f"Invalid input: {zde}")

        
