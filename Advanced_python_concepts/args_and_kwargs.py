#Example of args and kwargs in Python

# Example of args
def sum(*args): #args will be a tuple of all the values passed to sum function
    total = 0
    for num in args:
        total += num
    return total
print(sum(1, 2, 3, 4, 5))  # This will output 15
# In the above example, *args allows the function to accept any number of positional arguments. You are not limited to a specific number of arguments. 


# Example of kwargs
def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
        
marks(John=90, Alice=85, Bob=92)  # This will output the marks of each student
# In the above example, **kwargs allows the function to accept any number of keyword arguments. You can pass a variable number of named arguments to the function. Basically kwargs allows you to store multiple dictionaries within a single parameter.