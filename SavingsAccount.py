# refering class defined in another module/ file

from BankAccount import Bank_Account



class SavingsAccount(Bank_Account):
    def calculate_interest(self):
        # fetching balance and calculating interest as 5 % of the balance amount.
        interest = (self.get_balance()) * 5 / 100
        print(f"The saving account interest is - {interest}")
        return interest
    

 