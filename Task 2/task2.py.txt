import json
import os
from datetime import datetime

class BudgetTracker:
    def __init__(self, filename):
        self.filename = filename
        self.transactions = []
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.transactions = json.load(f)

    def save_transactions(self):
        with open(self.filename, 'w') as f:
            json.dump(self.transactions, f)

    def add_transaction(self, category, amount, transaction_type):
        self.transactions.append({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'category': category,
            'amount': amount,
            'type': transaction_type
        })
        self.save_transactions()

    def calculate_balance(self, income):
        total_expenses = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        total_income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'income')
        remaining_budget = income - total_expenses
        return remaining_budget, total_expenses, total_income

    def get_spending_trends(self):
        spending_trends = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                category = transaction['category']
                amount = transaction['amount']
                if category in spending_trends:
                    spending_trends[category] += amount
                else:
                    spending_trends[category] = amount
        return spending_trends

def main():
    filename = "transactions.json"
    budget_tracker = BudgetTracker(filename)

    while True:
        print("\n===== Budget Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Spending Trends")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            income = float(input("Enter income amount: "))
            budget_tracker.add_transaction('income', income, 'income')
            print("Income added successfully.")

        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_transaction(category, amount, 'expense')
            print("Expense added successfully.")

        elif choice == '3':
            income = float(input("Enter your total income: "))
            remaining_budget, total_expenses, total_income = budget_tracker.calculate_balance(income)
            print(f"Total Expenses: {total_expenses}")
            print(f"Total Income: {total_income}")
            print(f"Remaining Budget: {remaining_budget}")

        elif choice == '4':
            spending_trends = budget_tracker.get_spending_trends()
            print("Spending Trends:")
            for category, amount in spending_trends.items():
                print(f"{category}: {amount}")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
