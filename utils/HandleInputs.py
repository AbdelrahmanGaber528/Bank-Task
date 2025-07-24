from utils.Exceptions import InvalidAmountError

def get_float_input(prompt):
    """ get a positive float input from the user for balance ."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid Amount(Number).")


def get_valid_menu_choice():
    """Ask user for a menu choice until it's valid (1-4)."""
    while True:
        try:
            choice = int(input("Your choice: "))
            if choice not in [1, 2, 3, 4]:
                print("Please choose a valid option (1-4).")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")


def get_positive_amount(prompt):
    """Ask user for a positive amount until it's valid."""
    while True:
        try :
            amount = get_float_input(prompt)
            if amount < 0:
                raise InvalidAmountError()
            return amount
        except InvalidAmountError as e:
            print(e)
