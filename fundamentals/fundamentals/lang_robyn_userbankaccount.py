class bank_account:

    def __init__(self, interest_rate = .01, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        print(f'starting balance: ${self.balance}')
        self.balance += amount
        print(f'amount deposited: ${amount}')
        print(f'your balance is now: ${self.balance}')
        return self

    def withdraw(self, amount):
        print(f'starting balance: ${self.balance}')
        self.balance -= amount
        print(f'amount withdrawn: ${amount}')
        print(f'your balance is now: ${self.balance}')
        return self

    def display_account_info(self):
        print (f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        print(f'starting balance: ${self.balance}')
        if self.balance > 0:
            print(f"is your balance greater than 0? yes it is.")
            print(f'${self.balance * self.interest_rate} will be added to your balance.')
            self.balance += self.balance * self.interest_rate
            print(f'your balance is now: ${self.balance}')
            return self

class user:

    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount):
        print('')
        print("********************start making deposit********************")
        print(f"{self.name}'s starting account balance is ${self.account.balance}.")
        self.account.deposit(amount)
        print(f"{self.name}'s account balance is now ${self.account.balance}.")
        print("********************end making deposit********************")
        return self

    def make_withdrawal(self, amount):
        print('')
        print("********************start making withdrawal********************")
        print(f"{self.name}'s starting account balance is ${self.account.balance}.")
        self.account.withdraw(amount)
        print(f"{self.name}'s account balance is now ${self.account.balance}.")
        print("********************end making withdrawal********************")
        return self

    def display_user_balance(self):
        print('')
        print("********************start display user balance********************")
        self.account.display_account_info()
        print(f"{self.name}'s account balance is now ${self.account.balance}.")
        print("********************end display user balance********************")
        return self


robyn = user('Robyn Traci Lang', 'jetblackkinks@gmail.com', account = bank_account(.02, 500))
shep = user('Sheppard Dean', 'sdj@gmail.com', account = bank_account(.03, 700))

robyn.make_deposit(53).make_deposit(38).make_deposit(67).make_withdrawal(80)
robyn.display_user_balance()

shep.make_deposit(5000).make_deposit(6000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(100).make_withdrawal(100)
shep.display_user_balance()




# not yet able to figure out the Sensei and Senpai challenges.
# class bank_account:

#     def __init__(self, account_name, interest_rate = .01, balance = 0):
#         self.account_name = account_name
#         self.interest_rate = interest_rate
#         self.balance = balance

#     def deposit(self, amount):
#         print(f'starting balance: ${self.balance}')
#         self.balance += amount
#         print(f'amount deposited: ${amount}')
#         print(f'your balance is now: ${self.balance}')
#         return self

#     def withdraw(self, amount):
#         print(f'starting balance: ${self.balance}')
#         self.balance -= amount
#         print(f'amount withdrawn: ${amount}')
#         print(f'your balance is now: ${self.balance}')
#         return self

#     def display_account_info(self):
#         print (f'Balance: ${self.balance}')
#         return self

#     def yield_interest(self):
#         print(f'starting balance: ${self.balance}')
#         if self.balance > 0:
#             print(f"is your balance greater than 0? yes it is.")
#             print(f'${self.balance * self.interest_rate} will be added to your balance.')
#             self.balance += self.balance * self.interest_rate
#             print(f'your balance is now: ${self.balance}')
#             return self

# class user:

#     def __init__(self, name, email, bank_accounts = []):
#         self.name = name
#         self.email = email
#         self.bank_accounts = bank_accounts

#     def make_deposit_2(self, account_name, amount):
#         print('')
#         for i in range(len(self.bank_accounts)):
#             print("********************start making deposit********************")
#             print(f"{self.name} has ${self.bank_accounts[i]} in the account named '{account_name}'.")
#             self.bank_accounts[i].deposit(amount)
#             print(f"{self.name} now has ${self.bank_accounts[i]} in the account named '{account_name}'.")
#         print("********************end making deposit********************")
#         return self

#     def make_withdrawal_2(self, account_name, amount):
#         print('')
#         print("********************start making withdrawal********************")
#         print(f"{self.name} has ${self.bank_accounts.balance} in the account named '{account_name}'.")
#         self.account.withdraw(amount)
#         print(f"{self.name} now has ${self.account.balance} in the account named '{account_name}'.")
#         print("********************end making withdrawal********************")
#         return self

#     def display_user_balance(self):
#         print('')
#         print("********************start display user balance********************")
#         for i in range(len(self.bank_accounts)):
#             self.bank_accounts[i].display_account_info()
#             print(f"{self.name}'s account balance is now ${self.bank_accounts[i].balance}.")
#         print("********************end display user balance********************")
#         return self

#     def create_additional_account(self, account_name):
#         print('')
#         print("********************start create additional account********************")
#         new_account = bank_account(interest_rate = .01, balance = 0)
#         account_number = 1
#         account_name = f"robyns bank account {account_number}"
#         account_number += 1
#         self.bank_accounts.append(new_account)
#         print(f"A new account named {account_name} has been created for {self.name}.")
#         print("********************end create additional account********************")
#         return self


# robyn = user('Robyn Traci Lang', 'jetblackkinks@gmail.com', bank_accounts = bank_account())
# shep = user('Sheppard Dean', 'sdj@gmail.com', bank_accounts = bank_account())

# # robyn.make_deposit(53).make_deposit(38).make_deposit(67).make_withdrawal(80)
# # robyn.display_user_balance()

# # shep.make_deposit(5000).make_deposit(6000).make_withdrawal(50).make_withdrawal(50).make_withdrawal(100).make_withdrawal(100)
# # shep.display_user_balance()

# robyn.create_additional_account().make_deposit_2(account_name, 500).make_deposit_2('first account', 8000)



