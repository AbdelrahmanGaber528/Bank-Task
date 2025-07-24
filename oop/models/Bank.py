import random

class Bank:

    def __init__(self):
        self.__name = random.choice(['Cairo','Alex','Qatar'])

    def get_name(self):
        return self.__name
