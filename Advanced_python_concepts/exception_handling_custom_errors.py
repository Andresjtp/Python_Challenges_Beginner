# Example of Exception Handling and Custom Errors in Python

    # This is an example of exception handling so that the code won't crash when running, instead output an error message and thus continue running.
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(f"Sum is: {a / b}")
        
except Exception as e:
    print("Invalid input, please enter numeric values.", e)
        
        
# Example of raising an exception manually        
c = int(input("Enter another number: "))
d = int(input("Enter one more number: "))

if d == 0:
    raise ValueError("Please don't divide by 0") # this is an example of raising an exception manually. and stopping the program if this condition is met.

print(f"Division is: {c / d}")


# example of using else in excpetion handling
try: 
    a = 345/10
except Exception as e:
    print(e)
else:
    print("Hey I am Good")  # this block will run only if there is no exception in the try block
  
    
# example of using finally in exception handling
try:
    a = 345/0
except Exception as e:
    print(e)
finally:
    print("I will run no matter what")  # this block will run no matter what, whether there is an exception or not.