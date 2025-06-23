# -*- coding: utf-8 -*-
"""budgeter.ipynb

"""

def main():
    print("Welcome to the Budgeter App")
    initial_budget = float(input("What is your budget: "))
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input('Enter your choice (1, 2, 3): ')

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter the amount spent: "))
            expenses.append((description, amount))
            budget -= amount

        elif choice == "2":
            print("\n--- Budget Details ---")
            print(f"Initial budget: ${initial_budget:.2f}")
            print(f"Remaining budget: ${budget:.2f}")
            print("Expenses:")
            if not expenses:
                print("No expenses recorded yet.")
            else:
                for i, (desc, amnt) in enumerate(expenses, 1):
                    print(f"{i}. {desc} - ${amnt:.2f}")

        elif choice == "3":
            print("Exiting budget app, Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
main()
