
class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
    
    def search_by_name(self, name_search):
        for name, contact in self.contacts.items():
            if name_search.lower() == name.lower():
                print(f"{contact.name}, phone number: {contact.phone}. email: {contact.email}")
    
    def update_contact(self, name_search, updated_phone, updated_email):
        for name, contact in self.contacts.items():
            if name_search.lower() == name.lower():
                contact.phone = updated_phone
                contact.email = updated_email
                
    def delete_contact(self, name_search):
        for name in self.contacts:
            if name_search.lower() == name.lower():
                self.contacts.pop(name)
                print(f"deleted: {name}")
                return
            print("Contact not found")
    
    def display_contacts(self):
         if not self.contacts:
            print("No contacts in the contact book.")
            return
    
         print("\n--- All Contacts ---")
         for name, contact in self.contacts.items():
             print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
         print("--------------------\n")
                