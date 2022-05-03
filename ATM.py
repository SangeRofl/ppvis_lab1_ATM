class Bank:
    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

class Card:
    __count = 0
    def __init__(self, pin: str, balance: int = 0):
        self.__id = Card.__count
        Card.__count += 1
        self.__pin = pin
        self.__balance = balance
    def get_balance(self):
        return self.__balance

class Atm:
    def __init__(self, currend_card: Card = None):
        self.__storage = Storage()
        self.__current_card = current_card
    def show_balance(self):
        try:
            balance = self.__current_card.get_balance()
        except:
            print("ATM error: Card is not find")
    def withdraw(self, value: int):
        try:
            self.__storage.get_money(value)
        except StorageError as se:
            print(se)
            
        
        

class Storage:
    def __init__(self, banknotes: dict = {}):
        self.__banknotes = banknotes
    def get_money(self, value):
        pass
        

class Banknote:
    def __init__(self, value: int):
        self.__value = value
