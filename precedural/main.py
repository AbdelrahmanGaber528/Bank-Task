from utils.Exceptions import InsufficientFundsError
from utils.HandleInputs import get_float_input, get_valid_menu_choice, get_positive_amount
import random


"""Utility functions"""

def check_balance(acc):
    return acc["balance"]


def dispose(acc, value):
    acc['balance'] += value
    return "Successfully disposed"


def withdraw(acc, value):
    while True:
        try:
            current_balance = acc['balance']
            if value > current_balance:
                raise InsufficientFundsError()
            acc['balance'] -= value
            return "Successfully withdrawn"

        except InsufficientFundsError as err:
            print(err)



"""Main Program"""

bank_name = ["Cairo", "Alex", "Qatar"]
random_bank_name = random.choice(bank_name)

print(f"{'*' * 40} Welcome to {random_bank_name} Bank {'*' * 40}")


# Init account
account = {}

# Account name
account["name"] = input("Please enter your name: ").strip()

# Account balance
account["balance"] = get_float_input("Please enter your initial balance: ")

print(f"\nHello, {account['name']}")

while True:

    print("Choose an option:\n1: Check balance\n2: Deposit\n3: Withdraw\n4: Exit")

    choice = get_valid_menu_choice()

    if choice == 1:

        balance = check_balance(account)
        print(f"Your balance is: {balance}")

    elif choice == 2:
        amount = get_positive_amount("Enter amount to deposit: ")
        dispose(account, amount)
        print(f"New balance: {account['balance']}")

    elif choice == 3:
        amount = get_positive_amount("Enter amount to withdraw: ")
        withdraw(account, amount)
        print(f"New balance: {account['balance']}")

    elif choice == 4:
        print(f"Thank you for banking with {random_bank_name} Bank, {account['name']}!")
        break

