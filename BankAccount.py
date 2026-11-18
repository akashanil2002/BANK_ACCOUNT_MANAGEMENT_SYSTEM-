from abc import ABC, abstractmethod

# creating a class as an abstract class
# we cannot create an object of the abstract class - abstraction
class Bank_Account(ABC):

    # constructor of the class
    def __init__(self, balance = 0):
        # This is a private variable - encapsulated
        self.__balance = balance

    @property
    def acc_balance(self):
        return self.__balance

    # creating an abstract method
    # THis method should be inherited by the child class
    @abstractmethod
    def calculate_interest(self):
        pass


#it dispaly the balance amount
    def display_balance(self):
        # we are displaying a private variable 
        print('The available account balance is -', self.__balance)

     # To return the balance amount   
    def get_balance(self):  
        return self.__balance

    
    def deposit_amount(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance = self.__balance + deposit_amount
            print('The balance after deposit is -', self.__balance)
        else:
            print('Please provide a positive number as deposit')

    def withdraw_amount(self, withdraw_amount):
        if withdraw_amount <= 0:
            print('Please provide a positive withdrawal amount')

        elif withdraw_amount <= self.__balance:
            self.__balance = self.__balance - withdraw_amount
            print('The final balance is -', self.__balance)

        else:
            print('Do not have sufficient balance')





