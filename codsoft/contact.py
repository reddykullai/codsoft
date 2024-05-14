def add_contact(contact_list):
    contact_name = input("Enter the contact name: ")
    contact_phone = int(input("Enter the phone number: "))
    contact_email = input("Enter the email address: ")
    contact_address = input("Enter the address: ")
    contact_list[contact_name] = {
        'phone': contact_phone, 
        'email': contact_email, 
        'address': contact_address
    }
    print("Contact added successfully!")

def display_contacts(contact_list):
    for name, details in contact_list.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

def search_for_contact(contact_list):
    search_query = input("Enter the name or phone number to search: ")
    found_contact = False
    for name, details in contact_list.items():
        if search_query in name or str(search_query) == str(details['phone']):
            print(f"Found - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found_contact = True
    if not found_contact:
        print("No contact found.")

def update_existing_contact(contact_list):
    contact_name = input("Enter the name of the contact to update: ")
    if contact_name in contact_list:
        print("Enter new details (press enter to skip):")
        new_phone = input("New phone number: ")
        new_email = input("New email address: ")
        new_address = input("New address: ")
        
        if new_phone:
            contact_list[contact_name]['phone'] = new_phone
        if new_email:
            contact_list[contact_name]['email'] = new_email
        if new_address:
            contact_list[contact_name]['address'] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def remove_contact(contact_list):
    contact_name = input("Enter the name of the contact to delete: ")
    if contact_name in contact_list:
        del contact_list[contact_name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def run_contact_manager():
    contact_list = {}
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            add_contact(contact_list)
        elif user_choice == 2:
            display_contacts(contact_list)
        elif user_choice == 3:
            search_for_contact(contact_list)
        elif user_choice == 4:
            update_existing_contact(contact_list)
        elif user_choice == 5:
            remove_contact(contact_list)
        elif user_choice == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a choice between 1-6.")

if __name__ == "__main__":
    run_contact_manager()
