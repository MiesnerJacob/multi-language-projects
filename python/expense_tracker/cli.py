import argparse

def parse_command(command_args):
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="A simple CLI tool to track expenses",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("name", type=str, help="Expense name")
    add_parser.add_argument("amount", type=float, help="Expense amount")

    # View command
    subparsers.add_parser("view", help="View all expenses")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("id", type=str, help="Expense ID to delete")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search expenses")
    search_parser.add_argument("keyword", type=str, help="Keyword to search for")

    # Clear command
    subparsers.add_parser("clear", help="Clear all expenses")

    # Exit command
    subparsers.add_parser("exit", help="Exit the application")

    return parser.parse_args(command_args)