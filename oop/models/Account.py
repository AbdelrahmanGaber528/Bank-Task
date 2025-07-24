from oop.AccountMethods import get_last_id


class Account:

    __id = int(0)
    def __init__(self, name , balance):
        self.__id = get_last_id()
        self.__name = name # make private to perform the encapsulation
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def set_balance(self, balance):
        self.__balance = balance

