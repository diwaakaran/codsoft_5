import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

       
        self.label_name = tk.Label(root, text="Name:")
        self.label_phone = tk.Label(root, text="Phone:")
        self.label_email = tk.Label(root, text="Email:")

        self.entry_name = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_email = tk.Entry(root)

        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_phone.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.button_add.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_view.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_delete.grid(row=5, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()

        if name and phone and email:
            new_contact = Contact(name, phone, email)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

        self.clear_entries()

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact book is empty.")
        else:
            contact_list = "\n".join([f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def delete_contact(self):
        name_to_delete = self.entry_name.get()
        if not name_to_delete:
            messagebox.showerror("Error", "Please enter the name to delete.")
            return

        for contact in self.contacts:
            if contact.name.lower() == name_to_delete.lower():
                self.contacts.remove(contact)
                messagebox.showinfo("Success", f"Contact {name_to_delete} deleted successfully!")
                self.clear_entries()
                return

        messagebox.showerror("Error", f"Contact with name '{name_to_delete}' not found.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact found - Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
                return
        print(f"Contact with name '{name}' not found.")
        
    def delete_contact(self,name):
            for contact in self.contacts:
                if contact.name.lower()== name.lower():
                    print("Contact Deleted -{contact.name}, Phone: {contact.phone}, Email: {contact.email} ")
                    return

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Details:")
        print("1. Add Contact")
        print("2. View Contacts")    
        print("3. Search Contact")
        print("4. Exit")
        print("5. Delete Contact")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            search_name = input("Enter the name to search: ")
            contact_book.search_contact(search_name)

        elif choice == "4":
            print("Exiting Contact Book. Goodbye!")
        elif choice == "5":
            print("Delete Contact Book")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
