contacts = []  # सभी contacts यहाँ list में रखेंगे

def show_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if c['name'] == keyword or c['phone'] == keyword:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}, Address: {c['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    view_contacts()
    try:
        num = int(input("Enter contact number to update: "))
        if 1 <= num <= len(contacts):
            c = contacts[num - 1]
            c['name'] = input(f"Enter new name ({c['name']}): ") or c['name']
            c['phone'] = input(f"Enter new phone ({c['phone']}): ") or c['phone']
            c['email'] = input(f"Enter new email ({c['email']}): ") or c['email']
            c['address'] = input(f"Enter new address ({c['address']}): ") or c['address']
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        num = int(input("Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            contacts.pop(num - 1)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
