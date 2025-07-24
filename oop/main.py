from oop.service.BankOperations import check_balance, withdraw, dispose, save_account
from oop.models.Account import Account
from oop.models.Bank import Bank
from utils.HandleInputs import get_positive_amount, get_valid_menu_choice

# create Bank object
My_Bank = Bank()

print(f"{"*"*40} Welcome to {My_Bank.get_name()} Bank {"*"*40}")

# Create Account :
current_account = Account(input("Enter your Name: "),get_positive_amount("Enter You Balance: "))

# save account in file
save_account(current_account)

print(f"\nHello, {current_account.get_name()}\n")

while True:

    print("Choose options from the Menu : \n1-Check balance\n2-Withdraw\n3-Dispose\n4-Exit")
    choice = get_valid_menu_choice()

    if choice == 1:
        print(check_balance(current_account))

    elif choice == 2:
        amount = get_positive_amount("Enter Amount to withdraw: ")
        print(withdraw(current_account, amount))
        print(check_balance(current_account))

    elif choice == 3:
        amount = get_positive_amount("Enter Amount to deposit: ")
        print(dispose(current_account, amount))
        print(check_balance(current_account))

    elif choice == 4:
        print(f"Thanks To Use {My_Bank.get_name()} Bank , Come again .")
        break
