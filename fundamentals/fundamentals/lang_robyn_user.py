'''
Assignment: User
For this assignment you will create the user class and add a couple methods!

Attributes:
On instantiation of a user, the following attributes should be passed in as arguments:

first_name
last_name
email
age
'''

class User:
    def __init__(self, first_name, last_name, email, age, is_reward_member, gold_card_points):
        self.first_name = 'robyn'
        self.last_name = 'lang'
        self.email = 'jetblackkinks@gmail.com'
        self.age = 44
        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self, attribute):
        print()

    def enroll(self):
        if(self.is_reward_member = True):
            print('User already a member.')
        else:
            self.is_reward_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            self.gold_card_points = 0

robyn = User()

display_info(robyn)

enroll(robyn)

monique = User()

michelle = User()

spend_points(robyn, 50)

enroll(monique)

spend_points(monique, 80)

display_info(robyn)
display_info(monique)
display_info(michelle)

enroll(robyn)

spend_points(michelle)

'''
Also include default attributes:

is_rewards_member - default value of False
gold_card_points = 0
Methods:
display_info(self) - Have this method print all of the users' details on separate lines.
enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
spend_points(self, amount) - have this method decrease the user's points by the amount specified.
Ninja Bonuses:

Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

Add the display_info(self) method to the User class

In the outer scope, create a user instance and call the display_info method to test.

Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.

Make 2 more instances of the User class.

Implement the spend_points(self, amount) method

Have the first user spend 50 points

Have the second user enroll.

Have the second user spend 80 points

Call the display method on all the users.

BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.

BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
'''