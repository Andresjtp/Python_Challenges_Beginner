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


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


# Example for setters and getters in Python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    @property  # Getter
    def first_name(self):
        name_parts = self.name.split(" ")
        return name_parts[0]

        # both the getter and setter have teh same function name to make it easier.

    @first_name.setter  # Setter
    def first_name(self, first):
        name_parts = self.name.split(" ")
        new_name = f"{first} {name_parts[1]}"
        self.name = new_name


e = Student("John doe", "Computer Science")

# If you notice, the methods/functions created can now be used just like attributes/values but are actually functions being called. No need for "()" when calling the function when we use setters and getters.
print(e.first_name)
e.first_name = "Jack"
print(e.name)


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


# Example for Instance Method, Static Method and Class Method in Python
class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # This is an Instance Method (default)
    def print_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    # This is a Static Method
    @staticmethod
    def sum(a, b):
        result = a + b
        print(result)

    # This is a Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Alice", 50000)
e1.print_info()  # Calling the instance method

result = Employee.sum(10, 20)
print(f"Sum: {result}")
# Calling the static method. No need to create an object before calling a static Method however you can still call it using an object if needed (e1.sum(10, 20)) is also valid.

print(Employee.company)
e1.change_company("Google")  # Calling the class method using an object to change the company name of the class (not the specific object)
print(Employee.company)


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


# Example for Magic/Dunder Methods in Python 
class Book:
    def __init__(self, title, author): # Basic constructor
        self.title = title
        self.author = author

    def __str__(self):  # String representation of the object
        return f"'{self.title}' by {self.author}"

    def __repr__(self): # Official representation of the object/ used mainly for developers to debug
        return f"Book: {self.title!r}, author: {self.author!r})"

    def __len__(self):  # Length of the object
        return len(self.title)

b1 = Book("1984", "George Orwell")
print(str(b1))  # Calls __str__ method
print(repr(b1))  # Calls __repr__ method
print(len(b1))  # Calls __len__ method


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


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


# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------


