#Example of walrus operator in Python

# The walrus operator (:=) allows you to assign values to variables as part of an expression.
# This can make certain constructs more concise and readable.
# essentially, you don't need to assign a value to a variable in a separate line, you can do it inline within an expression.
# Example 1: Using walrus operator in a while loop

while(data:= input("Enter the value: ")):
    print(data)
    if data == "q":
        break
    
#This example will keep asking for input until the user enters "q". The walrus operator assigns the input value to the variable 'data' and checks if it's truthy in the while condition.