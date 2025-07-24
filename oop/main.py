from oop.BankOperations import check_balance, withdraw, dispose
from oop.models.Account import Account
from oop.models.Bank import Bank
from utils.HandleInputs import get_positive_amount, get_valid_menu_choice

My_Bank = Bank()

print(f"Welcome to {My_Bank.get_name()}")

# Create Account :

current_account = Account(input("Enter your Name: "),get_positive_amount("Enter You Balance: "))

while True:
    print("Choose options from the Menu : \n1-Check balance\n2-Withdraw\n3-Dispose\n4-Exit")
    choice = get_valid_menu_choice()

    if choice == 1:
        print(check_balance(current_account))

    elif choice == 2:
        amount = get_positive_amount("Enter Amount to withdraw: ")
        print(withdraw(current_account, amount))

    elif choice == 3:
        amount = get_positive_amount("Enter Amount to deposit: ")
        print(dispose(current_account, amount))

    elif choice == 4:
        print("Thanks To Use our Bank , Come again .")
        break
