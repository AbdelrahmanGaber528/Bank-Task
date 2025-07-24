
class InvalidAmountError(Exception):
    """Raised when deposit or withdraw amount is invalid."""

    # define the magic method or dunder method to print it
    def __str__(self):
        return "Amount should be positive , try again"

class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds balance."""
    def __str__(self):
        return "Invalid Amount of withdrawal , Balance is not enough , try again"

