import uuid

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        self.expenses.append({"id": str(uuid.uuid4()), "name": name, "amount": amount})
        print(f"Added expense: ${amount} for {name}")

    def view_expenses(self):
        print("Viewing all expenses...")
        for expense in self.expenses:
            print(f"{expense['id']}: {expense['name']} - ${expense['amount']}")

    def delete_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense["id"] != expense_id]
        print(f"Deleted expense with ID: {expense_id}")

    def search_expenses(self, keyword):
        print(f"Searching expenses with keyword: {keyword}")
        for expense in self.expenses:
            if keyword in expense["name"]:
                print(f"{expense['id']}: {expense['name']} - ${expense['amount']}")

    def clear_expenses(self):
        self.expenses = []
        print("Cleared all expenses!")