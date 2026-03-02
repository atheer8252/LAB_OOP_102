class BankAccount:
    
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder   # Encapsulation
        if initial_balance >= 0:
            self.__balance = initial_balance
        else:
            self.__balance = 0

    # Deposit Method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.__balance += amount
        return self.__balance

    # Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.__balance:
            raise Exception("Insufficient funds.")
        
        self.__balance -= amount
        return self.__balance

    # Get Balance
    def get_balance(self):
        return self.__balance

    # Get Account Holder
    def get_account_holder(self):
        return self.__account_holder