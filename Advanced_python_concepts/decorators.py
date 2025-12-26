# This is an example of a decorator in Python
def decorator(func):  # The decorator takes a function as an arguement
    def wrapper():  # The wrapper function wraps around the original function
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper  # The decorator returns the wrapper function


@decorator  # This applies the decorator to the say_hello function
def say_hello():
    print("Hello World!")


say_hello()
# Now when we call the say_hello function, it will be wrapped by the decorator and outputs the additional print statements.
# example output:
# Before the function is called.
# Hello World!
# After the function is called.