# 📇 Contact Book Application

## Challenge Overview

This challenge focuses on building a contact management system using Python's object-oriented programming (OOP) principles, dictionaries for data storage, and search algorithms.

**Core Skills Practiced:**
- Dictionaries
- Object-Oriented Programming (OOP)
- Searching algorithms
- Data management

---

## Structure

### Class: `Contact`
Represents an individual contact with three attributes:
- `name` - Contact's full name
- `phone` - Contact's phone number
- `email` - Contact's email address

### Class: `ContactBook`
Manages a collection of contacts using a dictionary data structure:
- `contacts` - Dictionary where keys are contact names and values are `Contact` objects

---

## Features Implementation

### 1. **Add Contact**
```python
def add_contact(self, contact):
    self.contacts[contact.name] = contact
```
- Stores the entire `Contact` object in the dictionary
- Uses the contact's name as the key for quick lookups
- Allows storing all contact information (name, phone, email) together

### 2. **Search by Name**
```python
def search_by_name(self, name_search):
    for name, contact in self.contacts.items():
        if name_search.lower() == name.lower():
            print(f"{contact.name}, phone number: {contact.phone}. email: {contact.email}")
```
- Iterates through all contacts in the dictionary
- Performs case-insensitive search using `.lower()`
- Accesses the Contact object's attributes to display information

### 3. **Update Contact**
```python
def update_contact(self, name_search, updated_phone, updated_email):
    for name, contact in self.contacts.items():
        if name_search.lower() == name.lower():
            contact.phone = updated_phone
            contact.email = updated_email
```
- Searches for the contact by name (case-insensitive)
- Directly modifies the Contact object's attributes
- Changes persist because we're modifying the object stored in the dictionary

### 4. **Delete Contact**
```python
def delete_contact(self, name_search):
    for name in self.contacts:
        if name_search.lower() == name.lower():
            self.contacts.pop(name)
            print(f"deleted: {name}")
            return
    print("Contact not found")
```
- Searches for the contact in the dictionary
- Uses `.pop(name)` to remove the key-value pair
- Returns immediately after deletion to avoid dictionary modification errors during iteration

### 5. **Display All Contacts**
```python
def display_contacts(self):
    if not self.contacts:
        print("No contacts in the contact book.")
        return
    
    print("\n--- All Contacts ---")
    for name, contact in self.contacts.items():
        print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    print("--------------------\n")
```
- Checks if the contact book is empty
- Iterates through all contacts and displays their information
- Formats output in a readable way

---

## Key Concepts Demonstrated

### Dictionary with Objects as Values
Instead of storing individual pieces of data, the code stores entire `Contact` objects:
```python
# Key: "John Doe" → Value: Contact(name="John Doe", phone="555-1234", email="john@email.com")
self.contacts[contact.name] = contact
```

This allows:
- All contact information to be grouped together
- Easy access to any attribute via the object (e.g., `contact.phone`, `contact.email`)
- Clean and maintainable code structure

### Object-Oriented Design
- **Encapsulation**: Contact data is encapsulated in the `Contact` class
- **Single Responsibility**: Each class has a clear purpose (Contact holds data, ContactBook manages operations)
- **Data Abstraction**: The internal dictionary structure is hidden from users of the class

### Case-Insensitive Search
All search operations use `.lower()` to ensure "John Doe", "john doe", and "JOHN DOE" are treated as the same contact.

---

## Usage Example

```python
# Create a contact book
book = ContactBook()

# Create and add contacts
john = Contact("John Doe", "555-1234", "john@email.com")
jane = Contact("Jane Smith", "555-5678", "jane@email.com")

book.add_contact(john)
book.add_contact(jane)

# Search for a contact
book.search_by_name("john doe")  # Case-insensitive

# Update contact information
book.update_contact("John Doe", "555-9999", "newemail@email.com")

# Display all contacts
book.display_contacts()

# Delete a contact
book.delete_contact("Jane Smith")
```
