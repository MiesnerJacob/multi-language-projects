from cli import parse_command
from core import ExpenseTracker

def main() -> None:
    """Main entry point for the Expense Tracker application."""
    print("Welcome to Expense Tracker!")
    print("Type '--help' to see available options or 'exit' to quit.")
    expense_tracker = ExpenseTracker()
    run_command_loop(expense_tracker)

def run_command_loop(expense_tracker: ExpenseTracker) -> None:
    """Runs the command loop for user input."""
    while True:
        try:
            user_input = get_user_input()
            if not user_input:
                continue

            args = parse_command(user_input.split())
            execute_command(expense_tracker, args)

        except SystemExit:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def get_user_input() -> str:
    """Prompts the user for input and returns it."""
    return input("expense-tracker> ").strip()

def execute_command(expense_tracker: ExpenseTracker, args) -> None:
    """Executes the command based on parsed arguments."""
    if args.command == "add":
        expense_tracker.add_expense(args.name, args.amount)
    elif args.command == "view":
        expense_tracker.view_expenses()
    elif args.command == "delete":
        print(args)
        expense_tracker.delete_expense(args.id)
    elif args.command == "search":
        expense_tracker.search_expenses(args.keyword)
    elif args.command == "clear":
        expense_tracker.clear_expenses()
    elif args.command == "exit":
        print("Goodbye!")
        raise SystemExit(0)
    else:
        print("Unknown command. Type '--help' for available options.")

if __name__ == "__main__":
    main()