
class Account:

    def __init__(self, name , balance):
        self.__name = name # make private to perform the encapsulation
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

