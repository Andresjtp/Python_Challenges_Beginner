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