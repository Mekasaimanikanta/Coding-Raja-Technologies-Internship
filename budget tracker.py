import sys

class BudgetTracker:
    def __init__(self):
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def show_summary(self):
        total_income = sum(item["amount"] for item in self.income)
        total_expenses = sum(item["amount"] for item in self.expenses)
        balance = total_income - total_expenses

        print("\n--- Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")

    def show_details(self):
        print("\n--- Income Details ---")
        for item in self.income:
            print(f"Description: {item['description']}, Amount: ${item['amount']:.2f}")

        print("\n--- Expense Details ---")
        for item in self.expenses:
            print(f"Description: {item['description']}, Amount: ${item['amount']:.2f}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Show Details")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            budget_tracker.add_income(amount, description)
            print("Income added successfully.")
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            budget_tracker.add_expense(amount, description)
            print("Expense added successfully.")
        elif choice == "3":
            budget_tracker.show_summary()
        elif choice == "4":
            budget_tracker.show_details()
        elif choice == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()