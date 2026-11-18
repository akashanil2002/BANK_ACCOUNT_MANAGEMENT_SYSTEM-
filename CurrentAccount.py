from BankAccount import Bank_Account
# Inheritance : we inherit methods and properties of parent class
class CurrentAccount(Bank_Account):


    def dummumymethod(self):
        print('This is a dummy method')
        
    def calculate_interest(self):
        interest = 0
        self.get_balance()
        print(f"Your current account interest is {interest}")
        return interest