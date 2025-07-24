from oop.models.Account import Account
from utils.Exceptions import InsufficientFundsError
from utils.file_manager import insert

def check_balance(account:Account):
    return f"Your Balance is {account.get_balance()}"

def withdraw(account: Account, amount: float): # REMOVE MONEY FROM BALANCE
    while True:
        try :
            current_balance = account.get_balance()
            if amount > current_balance:
                raise InsufficientFundsError()
            account.set_balance(current_balance - amount)
            return "Successfully withdrawn"

        except InsufficientFundsError as err:
            print(err)

def dispose(account: Account,amount: float): # add money to ACCOUNT
    current_balance = account.get_balance()
    account.set_balance(current_balance + amount)
    return "Successfully disposed"


def save_account(account: Account):
    insert(f"{account.get_id()} {account.get_name()}    {account.get_balance()}")


save_account(Account("faf",15464))
### This methods can be in the bank system , but need more handled

def update_account(account: Account):
    pass

def delete_account(id: int):
    pass
def load_accounts():
    pass

