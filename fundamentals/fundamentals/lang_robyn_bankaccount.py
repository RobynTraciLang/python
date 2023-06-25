class bank_account:

    # don't forget to add some default values for these parameters! 
    # I'm leaving this here to remind myself what I was missing when I was working on this assignment.
    def __init__(self, name, interest_rate = .01, balance = 0):
        self.name = name
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        print('')
        print(f'********************start deposit for {self.name}********************')
        print(f'starting balance: ${self.balance}')
        self.balance += amount
        print(f'amount deposited: ${amount}')
        print(f'your balance is now: ${self.balance}')
        print(f'********************end deposit for {self.name}********************')
        return self

    def withdraw(self, amount):
        print('')
        print(f'********************start withdrawal for {self.name}********************')
        print(f'starting balance: ${self.balance}')
        self.balance -= amount
        print(f'amount withdrawn: ${amount}')
        print(f'your balance is now: ${self.balance}')
        print(f'********************end withdrawal for {self.name}********************')
        return self

    def display_account_info(self):
        print('')
        print(f"********************start {self.name}'s account info display********************")
        print (f'Balance: ${self.balance}')
        print(f"********************end {self.name}'s account info display********************")
        return self

    def yield_interest(self):
        print('')
        print(f'********************start interest yield transaction for {self.name}********************')
        print(f'starting balance: ${self.balance}')
        if self.balance > 0:
            print(f"is {self.name}'s balance greater than 0? yes it is.")
            print(f'${self.balance * self.interest_rate} will be added to your balance.')
            self.balance += self.balance * self.interest_rate
            print(f'your balance is now: ${self.balance}')
            print(f'********************end interest yield transaction for {self.name}*******************')
            return self

robyns_account = bank_account('robyn traci lang', .02, 500)
sheps_account = bank_account('sheppard dean, junior', .03, 700)

robyns_account.deposit(53).deposit(38).deposit(67).withdraw(80)
robyns_account.yield_interest().display_account_info()

sheps_account.deposit(5000).deposit(6000).withdraw(50).withdraw(50).withdraw(100).withdraw(100)
sheps_account.yield_interest().display_account_info()

print('')
print("While I'm learning, I will be using a lot of print statements so I can use my assignments as a reference when I forget concepts, and of course so I can make sure I know what I'm doing lol. Thanks for showing me how, Robert!")

'''
For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

Let's first just get some more practice writing classes by writing a new BankAccount class.

The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

The class should also have the following methods:

deposit(self, amount) - increases the account balance by the given amount
withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
display_account_info(self) - print to the console: eg. "Balance: $100"
yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
'''