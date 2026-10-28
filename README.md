# 🏦 Banking System — Console Application

A simple console-based banking application developed using Python. The application allows users to deposit money, withdraw money, and check their current account balance.

The account balance is stored in a text file so that the balance persists even after the application is closed and restarted.

---

## 📌 Project Overview

### Project Name

**Banking System — Console Application**

### Project Type

Python Console Application

### Purpose

The purpose of this project is to build a beginner-friendly banking application while practicing fundamental Python programming concepts such as:

- Functions
- Conditional statements
- Loops
- File handling
- Input validation
- Exception handling
- Menu-driven programming

---

## 🎯 Objectives

The application is designed to:

1. Allow users to deposit money.
2. Allow users to withdraw money.
3. Display the current account balance.
4. Store the balance permanently in a file.
5. Validate user input.
6. Prevent withdrawals when the account has insufficient funds.
7. Handle invalid or non-numeric input without crashing.
8. Provide a simple and clear console interface.

---

## 🛠️ Technologies Used

- **Python 3.x**
- Python File Handling
- Python Functions
- Conditional Statements
- Loops
- Exception Handling
- Input Validation

---

## 📂 Project Structure

```text
banking_app/
│
├── bank.py
├── account.txt
├── README.md
└── banking_system_output.png
```

### File Description

| File | Description |
|---|---|
| `bank.py` | Main Python application |
| `account.txt` | Stores the current account balance |
| `README.md` | Project documentation |
| `banking_system_output.png` | Screenshot of application output |

---

# ⚙️ Requirements

Before running the project, make sure Python 3.x is installed on your computer.

Recommended:

```text
Python 3.8 or higher
```

A code editor such as the following can be used:

- Visual Studio Code
- PyCharm Community Edition
- Sublime Text
- Notepad++

---

# 🚀 Installation and Setup

## Step 1 — Install Python

Download and install Python 3.x.

Verify the installation using:

```bash
python --version
```

Example:

```text
Python 3.12.4
```

If `python` does not work on your system, try:

```bash
python3 --version
```

---

## Step 2 — Create the Project Folder

Create a folder named:

```text
banking_app
```

---

## Step 3 — Create the Required Files

Inside the folder, create:

```text
bank.py
account.txt
README.md
```

The application will also create `account.txt` automatically if the file does not exist.

---

## Step 4 — Initialize the Account Balance

Open:

```text
account.txt
```

and enter:

```text
0
```

This represents the initial account balance.

---

# ▶️ How to Run the Application

Open the terminal inside the `banking_app` folder.

Run:

```bash
python bank.py
```

Alternatively:

```bash
python3 bank.py
```

The application will display the banking menu.

---

# 🏦 Banking System Menu

When the application starts, the following menu is displayed:

```text
==============================
       BANKING SYSTEM
==============================
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
==============================
Enter your choice:
```

The user can select one of the four available options.

---

# 💰 1. Deposit Money

The deposit option allows the user to add money to the account.

### Example

```text
Enter your choice: 1
Enter deposit amount: ₹1000

Deposit successful!
Deposited Amount: ₹1000.00
New Balance: ₹1000.00
```

The updated balance is saved to:

```text
account.txt
```

---

# 💸 2. Withdraw Money

The withdrawal option allows the user to remove money from the account.

The application first checks whether sufficient balance is available.

### Example

```text
Enter your choice: 2
Enter withdrawal amount: ₹300

Withdrawal successful!
Withdrawn Amount: ₹300.00
Remaining Balance: ₹700.00
```

The updated balance is saved to the account file.

---

# 💳 3. Check Balance

The balance option displays the current account balance.

### Example

```text
Enter your choice: 3

Current Balance: ₹700.00
```

---

# 🚪 4. Exit

Selecting option `4` exits the application.

### Example

```text
Enter your choice: 4

Thank you for using the Banking System.
Goodbye!
```

---

# 🔐 Input Validation

The application contains input validation to prevent invalid transactions.

## Positive Deposit Amount

The deposit amount must be greater than zero.

Invalid:

```text
Enter deposit amount: ₹-100
```

Output:

```text
Error: Deposit amount must be positive.
```

---

## Positive Withdrawal Amount

The withdrawal amount must be greater than zero.

Invalid:

```text
Enter withdrawal amount: ₹-50
```

Output:

```text
Error: Withdrawal amount must be positive.
```

---

## Insufficient Balance

The application prevents users from withdrawing more money than their current balance.

Example:

```text
Current Balance: ₹700.00

Enter withdrawal amount: ₹1000
```

Output:

```text
Error: Insufficient balance.
Current Balance: ₹700.00
```

The balance is not changed.

---

## Invalid Numeric Input

The application handles non-numeric input using exception handling.

Example:

```text
Enter deposit amount: ₹abc
```

Output:

```text
Error: Please enter a valid number.
```

The program does not crash.

---

## Invalid Menu Choice

If the user enters an option other than 1, 2, 3, or 4:

```text
Enter your choice: 7
```

Output:

```text
Error: Invalid choice.
Please select an option from 1 to 4.
```

---

# 💾 File-Based Data Storage

The application uses:

```text
account.txt
```

to store the current account balance.

For example:

```text
700.0
```

represents a balance of ₹700.

### Deposit

```text
Current balance
       ↓
Add deposit amount
       ↓
Updated balance
       ↓
Save to account.txt
```

### Withdrawal

```text
Current balance
       ↓
Check sufficient balance
       ↓
Subtract withdrawal amount
       ↓
Updated balance
       ↓
Save to account.txt
```

---

# 🔄 Balance Persistence

One important feature of the application is balance persistence.

For example, suppose the balance is:

```text
₹700
```

After closing the program, run it again:

```bash
python bank.py
```

Select:

```text
3
```

The application reads the balance from `account.txt` and displays:

```text
Current Balance: ₹700.00
```

Therefore, the balance is maintained between program executions.

---

# 🧩 Application Functions

The application is divided into modular functions.

## `read_balance()`

Reads the current balance from `account.txt`.

Responsibilities:

- Open the balance file.
- Read the stored balance.
- Convert it to a numeric value.
- Return the balance.
- Create the file with an initial balance of `0` if the file does not exist.

---

## `write_balance(balance)`

Stores the updated balance in `account.txt`.

Example:

```text
700.0
```

---

## `deposit(amount)`

Handles money deposits.

Responsibilities:

- Validate the deposit amount.
- Read the current balance.
- Add the deposit amount.
- Save the updated balance.
- Display a success message.

---

## `withdraw(amount)`

Handles money withdrawals.

Responsibilities:

- Validate the withdrawal amount.
- Read the current balance.
- Check sufficient funds.
- Subtract the withdrawal amount.
- Save the updated balance.
- Display a success or error message.

---

## `check_balance()`

Reads and displays the current account balance.

Example:

```text
Current Balance: ₹700.00
```

---

## `main()`

Controls the main application.

Responsibilities:

- Display the menu.
- Accept the user's choice.
- Call the appropriate function.
- Continue displaying the menu until the user chooses Exit.

The application uses a `while True` loop to keep running until option `4` is selected.

---

# 🧪 Testing

The application was tested using the following scenarios.

| Test Case | Input | Expected Result |
|---|---|---|
| Deposit money | ₹1000 | Balance becomes ₹1000 |
| Withdraw money | ₹300 | Balance becomes ₹700 |
| Check balance | Option 3 | Displays ₹700 |
| Insufficient balance | Withdraw ₹1000 with ₹700 balance | Error message |
| Negative deposit | -₹100 | Error message |
| Negative withdrawal | -₹100 | Error message |
| Invalid amount | `abc` | Error message |
| Invalid menu choice | `7` | Error message |
| Restart application | Option 3 after restart | Previous balance remains |

---

# 🖥️ Sample Application Output

### Deposit

```text
==============================
       BANKING SYSTEM
==============================
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
==============================
Enter your choice: 1
Enter deposit amount: ₹1000

Deposit successful!
Deposited Amount: ₹1000.00
New Balance: ₹1000.00
```

### Withdrawal

```text
Enter your choice: 2
Enter withdrawal amount: ₹300

Withdrawal successful!
Withdrawn Amount: ₹300.00
Remaining Balance: ₹700.00
```

### Balance Check

```text
Enter your choice: 3

Current Balance: ₹700.00
```

### Insufficient Balance

```text
Enter your choice: 2
Enter withdrawal amount: ₹1000

Error: Insufficient balance.
Current Balance: ₹700.00
```

### Invalid Input

```text
Enter your choice: 1
Enter deposit amount: ₹abc

Error: Please enter a valid number.
```

---

# 📸 Project Screenshot

The project includes a screenshot demonstrating the application's console output, including banking operations and validation results.

Screenshot:

```text
banking_system_output.png
```

---

# 📋 Project Requirements Checklist

- [x] Python 3.x application
- [x] Console-based user interface
- [x] Deposit operation
- [x] Withdrawal operation
- [x] Balance checking
- [x] File-based balance storage
- [x] Automatic file creation
- [x] Positive amount validation
- [x] Insufficient balance validation
- [x] Invalid input handling
- [x] `try-except` error handling
- [x] Functions for modular structure
- [x] Menu-driven application
- [x] Balance persistence
- [x] README documentation
- [x] Application output screenshot

---

# 🎓 Learning Outcomes

Through this project, the following Python concepts were practiced:

### Python Fundamentals

- Variables
- Data types
- Operators
- Conditional statements
- Loops

### Functions

- Creating functions
- Function parameters
- Returning values
- Modular programming

### File Handling

- Opening files
- Reading files
- Writing files
- Handling missing files

### Exception Handling

- `try`
- `except`
- `ValueError`
- `FileNotFoundError`

### Input Validation

- Positive number validation
- Numeric input validation
- Balance validation
- Menu choice validation

### Application Design

- Menu-driven programming
- Separating functionality into functions
- Persistent file-based storage

---

# 🔮 Possible Future Improvements

The current project is intentionally kept simple as a beginner-level console application.

Possible future improvements include:

- Multiple bank accounts
- Account numbers
- User authentication
- Transaction history
- Transfer money between accounts
- JSON or database-based storage
- GUI interface
- REST API
- Database integration

These features are outside the scope of the current project.

---

# 👨‍💻 Author

**B B Naik**

Python Developer Internship Project

---

# 📄 License

This project was developed as part of a Python Developer Internship project for educational and learning purposes.