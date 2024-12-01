# Python Project

## Overview
This project is a simple command-line interface (CLI) tool designed to help users track their expenses. It allows users to add, view, delete, search, and clear expenses efficiently.

## Project
The Expense Tracker application is built using Python and utilizes a straightforward command-line interface for user interaction. It is designed to be easy to use and understand, making it suitable for anyone looking to manage their personal finances.

## Features
- Add new expenses with a name and amount.
- View all recorded expenses.
- Delete specific expenses by ID.
- Search for expenses using keywords.
- Clear all expenses at once.
- Exit the application gracefully.

## Learning Objectives
- Understand the basics of Python programming.
- Learn how to build a command-line application.
- Gain experience with data management in Python.
- Explore the use of external libraries for argument parsing.

## Requirements
- Python 3.6 or higher
- `argparse` library (included in the standard library)
- `uuid` library (included in the standard library)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```
2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the Expense Tracker application, execute the following command in your terminal:

## Examples
- To add an expense:
  ```
  add Coffee 3.50
  ```
- To view all expenses:
  ```
  view
  ```
- To delete an expense:
  ```
  delete <expense_id>
  ```
- To search for an expense:
  ```
  search Coffee
  ```
- To clear all expenses:
  ```
  clear
  ```
- To exit the application:
  ```
  exit
  ```

## Code Structure
- `main.py`: The main entry point of the application.
- `cli.py`: Handles command parsing and user input.
- `core.py`: Contains the `ExpenseTracker` class and its methods for managing expenses.
- `LICENSE`: The license file for the project.

## Further Reading
- [Python Documentation](https://docs.python.org/3/)
- [Argparse Documentation](https://docs.python.org/3/library/argparse.html)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.