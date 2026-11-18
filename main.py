from CurrentAccount import CurrentAccount
from SimpleAccount import SimpleAccount
from BankAccount import Bank_Account
from SavingsAccount import SavingsAccount
# create an object of current account



# create an object of the current account
# sAccount1 = SimpleAccount()
# sAccount1.method1()

# not possible because we cnnot create a object using abstract class
# bankAcc1 = Bank_Account()
# bankAcc1.deposit_amount()

ca1 = CurrentAccount()
# ca1.dummumymethod()
# ca1.deposit_amount(1000)
# # the acc_balnce will only be able if we add a setter or cannot be accesed from outside.
# print(f"balance amount is : {ca1.acc_balance}")

# # other way of displaying balance use the function from the parent class
# ca1.display_balance()
# ca1.__balance
# print(ca1.__balance)

ca1.deposit_amount(1700)
ca1.display_balance()

# ca1.deposit_amount(-1700)
# ca1.display_balance()

# ca1.withdraw_amount(1700)
# ca1.display_balance()

# ca1.withdraw_amount(2000)
# ca1.display_balance()

ca1.calculate_interest()





sa1 = SavingsAccount()
sa1.display_balance()

sa1.deposit_amount(1800)
sa1.display_balance()

sa1.withdraw_amount(1700)
sa1.display_balance()


# sa1.withdraw_amount(1700)
# sa1.display_balance()

sa1.calculate_interest()

print('********************************************************Hello ********************')