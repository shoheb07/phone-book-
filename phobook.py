import csv
import os

FILE_NAME = "phonebook.csv"

# Initialize file
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])

# Add contact
def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("Contact added successfully.")

# View contacts
def view_contacts():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

# Search contact
def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if keyword.lower() in row[0].lower() or keyword in row[1]:
                print(f"Found → Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True

    if not found:
        print("Contact not found.")

# Update contact
def update_contact():
    name = input("Enter name to update: ")
    rows = []
    updated = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0].lower() == name.lower():
                phone = input("New Phone: ")
                email = input("New Email: ")
                rows.append([row[0], phone, email])
                updated = True
            else:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("Contact updated." if updated else "Contact not found.")

# Delete contact
def delete_contact():
    name = input("Enter name to delete: ")
    rows = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row[0].lower() != name.lower():
                rows.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print("Contact deleted." if deleted else "Contact not found.")

# Main menu
def main():
    init_file()
    while True:
        print("\n📞 PHONE BOOK")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose option: ")

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
            break
        else:
            print("Invalid choice.")

main()
