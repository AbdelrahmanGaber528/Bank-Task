from oop.models.Account import Account
from utils.Exceptions import InsufficientFundsError




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




### This methods can be in the bank system , but need more handled

from utils.file_manager import insert
from oop.service.AccountMethods import get_last_id

def save_account(account: Account):
    insert(f"{get_last_id()}    {account.get_name()}    {account.get_balance()}")

def update_account(account: Account):
    pass

def delete_account(id: int):
    pass
def load_accounts():
    pass

