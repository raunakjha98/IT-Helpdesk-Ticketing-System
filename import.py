import csv
import os
from datetime import datetime

FILE_NAME = "tickets.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ticket ID", "User Name", "Issue", "Priority", "Status", "Created On"])

def create_ticket():
    ticket_id = input("Enter Ticket ID: ")
    user_name = input("Enter User Name: ")
    issue = input("Describe the Issue: ")
    priority = input("Enter Priority (Low/Medium/High): ")
    status = "Open"
    created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ticket_id, user_name, issue, priority, status, created_on])

    print("✅ Ticket Created Successfully!")

def view_tickets():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def update_ticket_status():
    ticket_id = input("Enter Ticket ID to Update: ")
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row and row[0] == ticket_id:
            print(f"Current Status: {row[4]}")
            new_status = input("Enter New Status (Open/In Progress/Resolved/Closed): ")
            row[4] = new_status
            print("✅ Ticket Status Updated!")

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def main_menu():
    initialize_file()

    while True:
        print("\n===== IT HELPDESK TICKETING SYSTEM =====")
        print("1. Create New Ticket")
        print("2. View All Tickets")
        print("3. Update Ticket Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket_status()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
