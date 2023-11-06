import re  


contacts = {}


def add_contact(name, email, phone):
    if name in contacts:
        print(f"{name} already exists in the address book.")
    else:
        if len(phone) == 10 and phone.isdigit():
            email_pattern = r"^(?=(.*[A-Za-z]){5,})(?=(.*\d){1,})(?=(.*[!@#$%^&*()_+|\\[\]{};:'\",.<>?]){1,}).{8,}$"
            if re.match(email_pattern, email):
                contacts[name] = {"email": email, "phone": phone}
                print(f"Contact for {name} added successfully.")
            else:
                print("Incorrect email format. The email must contain at least 5 alphabetic characters, at least 1 number, and at least 1 special character, in a total of 8 characters.")
        else:
            print("Incorrect contact number. The phone number must have exactly 10 digits.")


def view_contact(name):
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
    else:
        print(f"{name} not found in the address book.")


def update_contact(name, email, phone):
    if name in contacts:
        if len(phone) == 10 and phone.isdigit():
            email_pattern = r"^(?=(.*[A-Za-z]){5,})(?=(.*\d){1,})(?=(.*[!@#$%^&*()_+|\\[\]{};:'\",.<>?]){1,}).{8,}$"
            if re.match(email_pattern, email):
                contacts[name] = {"email": email, "phone": phone}
                print(f"Contact for {name} updated successfully.")
            else:
                print("Incorrect email format. The email must contain at least 5 alphabetic characters, at least 1 number, and at least 1 special character, in a total of 8 characters.")
        else:
            print("Incorrect contact number. The phone number must have exactly 10 digits.")
    else:
        print(f"{name} not found in the address book.")


def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted successfully.")
    else:
        print(f"{name} not found in the address book.")


while True:
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        add_contact(name, email, phone)
    elif choice == "2":
        name = input("Enter name to view: ")
        view_contact(name)
    elif choice == "3":
        name = input("Enter name to update: ")
        email = input("Enter updated email: ")
        phone = input("Enter updated phone: ")
        update_contact(name, email, phone)
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


