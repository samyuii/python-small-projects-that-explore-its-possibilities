import os


def create_entry(date, content):
    with open(f"{date}.txt", "w") as file:
        file.write(content)
    print("Diary entry created successfully!")

def read_entry(date):
    try:
        with open(f"{date}.txt", "r") as file:
            content = file.read()
            print(f"Diary entry for {date}:\n")
            print(content)
    except FileNotFoundError:
        print("Diary entry not found.")


while True:
    print("Welcome to the Personal Diary App!")
    print("1. Create a new entry")
    print("2. Read an existing entry")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        date = input("Enter the date (e.g., YYYY-MM-DD): ")
        content = input("Write your diary entry:\n")
        create_entry(date, content)
        print("\n")
    elif choice == "2":
        date = input("Enter the date of the entry to read (e.g., YYYY-MM-DD): ")
        read_entry(date)
        print("\n")
    elif choice == "3":
        print("Thanks for using the Personal Diary App. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        print("\n")
