from abc import ABC, abstractmethod
from termcolor import colored


class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Client(Person):
    # overwrite to include extra args
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account = None

        # feedback
        msg = f'Client {self.name} inserted in the system.'
        print(colored(msg, 'blue'))

    def assign_account(self, account):
        self.account = account

        # feedback
        print()
        msg = f'Client {self._name} assigned account:'
        print(colored(msg, 'cyan'))
        self.account.details()


class Account(ABC):
    def __init__(self, ag, ac, am):
        self.ag = ag
        self.ac = ac
        self.am = am

        # feedback
        print()
        msg = 'Account added to the system'
        print(colored(msg, 'cyan'))
        self.details()

    def deposit(self, value):
        self.am += value

        # feedback
        msg = '\nDeposit confirmed'
        print(colored(msg, 'cyan'))
        self.details()

    def details(self):
        msg = f'AG: {self.ag} | ' \
              f'AC: {self.ac} | ' \
              f'AM: {self.am} '
        print(colored(msg, 'grey'))

    @abstractmethod
    def takeout(self, value): pass


class Savings(Account):
    # All we need for this one is to fill our abstract methods:
    def takeout(self, value):
        if self.am < value:
            warn = '\nNot enough money in your account.'
            print(colored(warn, 'red'))
            self.details()
            return

        self.am -= value

        msg = f'\nTakeout successful'
        print(colored(msg, 'green'))
        self.details()


class Regular(Account):
    # This time, we must overwrite INIT to add extra args
    def __init__(self, ag, ac, am, limit=100):
        super().__init__(ag, ac, am)  # send parent args
        self._limit = limit  # include extra arg

    def takeout(self, value):
        if (self.am + self._limit) < value:
            warn = f'\nYou have a limit of {self._limit} on your account.'
            print(colored(warn, 'red'))
            self.details()
            return

        self.am -= value

        msg = '\nTakeout successful'
        print(colored(msg, 'green'))
        self.details()


class Bank:
    def __init__(self):
        self.agencies = [1111, 2222, 3333]
        self.clients = []
        self.accounts = []

    def insert_client(self, client: Client):
        self.clients.append(client)

    def insert_account(self, account: Account):
        self.accounts.append(account)

    def authenticate(self, client: Client):
        if client not in self.clients:
            print('Client not found in database.')
            return False
        if client.account not in self.accounts:
            print('Account not found in database.')
            return False
        if client.account.ag not in self.agencies:
            print('Agency not found.')
            return False

        return True
