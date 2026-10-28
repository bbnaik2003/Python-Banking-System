# Banking System - Console Application
# Project 1 - Python Developer Internship

def read_balance():
    """Read the current balance from account.txt."""

    try:
        with open("account.txt", "r") as file:
            balance = file.read().strip()

            if balance == "":
                return 0.0

            return float(balance)

    except FileNotFoundError:
        # Create the file with initial balance 0
        write_balance(0)
        return 0.0

    except ValueError:
        print("Error: Invalid balance data in account.txt")
        return 0.0


def write_balance(balance):
    """Save the current balance to account.txt."""

    with open("account.txt", "w") as file:
        file.write(str(balance))


def deposit(amount):
    """Deposit money into the account."""

    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return

    balance = read_balance()
    balance += amount

    write_balance(balance)

    print(f"Deposit successful!")
    print(f"Deposited Amount: ₹{amount:.2f}")
    print(f"New Balance: ₹{balance:.2f}")


def withdraw(amount):
    """Withdraw money from the account."""

    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return

    balance = read_balance()

    if amount > balance:
        print("Error: Insufficient balance.")
        print(f"Current Balance: ₹{balance:.2f}")
        return

    balance -= amount

    write_balance(balance)

    print("Withdrawal successful!")
    print(f"Withdrawn Amount: ₹{amount:.2f}")
    print(f"Remaining Balance: ₹{balance:.2f}")


def check_balance():
    """Display the current account balance."""

    balance = read_balance()

    print(f"Current Balance: ₹{balance:.2f}")


def main():
    """Main menu of the banking application."""

    while True:

        print("\n" + "=" * 30)
        print("       BANKING SYSTEM")
        print("=" * 30)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        print("=" * 30)

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            try:
                amount = float(input("Enter deposit amount: ₹"))
                deposit(amount)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "2":

            try:
                amount = float(input("Enter withdrawal amount: ₹"))
                withdraw(amount)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "3":

            check_balance()

        elif choice == "4":

            print("Thank you for using the Banking System.")
            print("Goodbye!")
            break

        else:

            print("Error: Invalid choice.")
            print("Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()