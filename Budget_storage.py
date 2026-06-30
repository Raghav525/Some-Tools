import os
from datetime import datetime

def save_expense(message):
    with open("Text Files/expenses.txt", "a") as file:
        file.write(message + "\n")

def view_expenses():
    expenses, bad_lines, valid_lines = load_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    if bad_lines:
        print(f"\n{len(bad_lines)} corrupted lines found.")
        choice = input("Do you want to clean the file? (y/n): ").lower().strip()
        if choice == "y":
            clean_file(valid_lines, bad_lines)
            print("File cleaned. Corrupted lines moved to bad_expenses.txt.")

    print("\nYour Expenses:\n")

    for expense in expenses:
        print(format_expense(expense))

def add_expense(date, category, price, amount, name):
    if price <= 0 or amount <= 0:
        return None

    total = price * amount

    return {
        "date": date,
        "amount": total,
        "category": category,
        "name": name
    }

def format_expense(expense):
    return f"{expense['date']}|{expense['category']}|{expense['name']}|{expense['amount']}"

def load_expenses(filename =  "Text Files/expenses.txt"):
    expenses = []
    bad_lines = []
    valid_lines = []

    if not os.path.exists(filename):
        return expenses, bad_lines, valid_lines

    with open(filename, "r") as f:
        for line_number, line in enumerate(f, start=1):
            original_line = line

            if not line.strip():
                continue

            parts = line.strip().split("|")

            if len(parts) != 4:
                bad_lines.append((line_number, line, "Invalid field count"))
                continue

            date, category, name, amount = [p.strip() for p in parts]

            if not date or not category or not name or not amount:
                bad_lines.append((line_number, line, "Empty field"))
                continue

            try:
                amount = float(amount)
            except ValueError:
                bad_lines.append((line_number, line, "Invalid amount"))
                continue

            expense = {
                "date": date,
                "category": category,
                "name": name,
                "amount": amount
            }

            expenses.append(expense)
            valid_lines.append(original_line)

    return expenses, bad_lines, valid_lines

def clean_file(valid_lines, bad_lines, filename="Text Files/expenses.txt"):
    if bad_lines:
        with open("Text Files/bad_expenses.txt", "w") as bad_file:
            for line_number, line_content, reason in bad_lines:
                bad_file.write(f"Line {line_number}: {line_content} - {reason}\n")

        with open(filename, "w") as f:
            f.writelines(valid_lines)

def search_by_date():
    date_input = input("Enter the date to search for (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expenses, _, _ = load_expenses()
    found = False

    for expense in expenses:
        if expense["date"] == date_input:
            print(format_expense(expense))
            found = True

    if not found:
        print(f"No expenses found for {date_input}.")

def search_by_category():
    category_input = input("Enter the category to search for: ").lower().strip()
    expenses, _, _ = load_expenses()
    found = False

    for expense in expenses:
        if expense["category"].lower() == category_input:
            print(format_expense(expense))
            found = True

    if not found:
        print(f"No expenses found for category '{category_input}'.")

def total_by_date():
    date = input("Enter the date to search for (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expenses, _, _ = load_expenses()
    total = 0
    found = False

    for expense in expenses:
        if date == expense["date"]:
            total += expense["amount"]
            found = True

    if not found:
        print(f"Records not found for date: {date}")
    else:
        print(f"Total for {date} is {total}")

def total_by_category():
    category = input("Enter the category to do total for: ").lower().strip()
    expenses, _, _ = load_expenses()
    total = 0
    found = False

    for expense in expenses:
        if category == expense["category"].lower():
            total += expense["amount"]
            found = True

    if not found:
        print(f"Records not found for category: {category}")
    else:
        print(f"Total for category '{category}' is: {total}")

def total_ui():
    while True:
        print("\nTotal by:")
        print("1. Date")
        print("2. Category")
        print("3. Back to Main Menu")

        choice = input("Enter the number of your choice: ").lower().strip()

        if choice in ["1", "date"]:
            total_by_date()
        elif choice in ["2", "category"]:
            total_by_category()
        elif choice in ["3", "back", "mainmenu"]:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def search_ui():
    while True:
        print("\nSearch by:")
        print("1. Date")
        print("2. Category")
        print("3. Back to Main Menu")

        choice = input("Enter the number of your choice: ").lower().strip()

        if choice in ["1", "date"]:
            search_by_date()
        elif choice in ["2", "category"]:
            search_by_category()
        elif choice in ["3", "back", "mainmenu"]:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def add_expense_ui():
    date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter the category: ").lower().strip()
    name = input("Enter the name: ").lower().strip()
    price_input = input("Enter the price: ").strip()
    amount_input = input("Enter the quantity: ").strip()

    if not name or "|" in name:
        print("Invalid name.")
        return

    if not category or "|" in category:
        print("Invalid category.")
        return

    try:
        price = float(price_input)
        amount = int(amount_input)
    except ValueError:
        print("Invalid input for price or amount.")
        return

    expense = add_expense(date, category, price, amount, name)

    if expense is None:
        print("Price and quantity must be greater than zero.")
        return

    formatted = format_expense(expense)
    save_expense(formatted)

    print("Expense added successfully!")

def menu():
    while True:
        print("\nSelect an option:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. View Total")
        print("5. Exit")

        choices = {
            "1": add_expense_ui,
            "addexpense": add_expense_ui,
            "add": add_expense_ui,
            "2": view_expenses,
            "viewexpenses": view_expenses,
            "view": view_expenses,
            "3": search_ui,
            "searchexpenses": search_ui,
            "search": search_ui,
            "4": total_ui,
            "total": total_ui,
            "viewtotal": total_ui,
        }

        choice = input("Enter the number of your choice: ").lower().strip()

        if choice in choices:
            choices[choice]()
        elif choice in ["5", "exit"]:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu()
