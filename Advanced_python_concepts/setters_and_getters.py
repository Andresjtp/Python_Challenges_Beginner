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