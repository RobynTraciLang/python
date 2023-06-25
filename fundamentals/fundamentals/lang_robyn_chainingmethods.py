class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_reward_member = False
        self.gold_card_points = 0

    def display_info(self):
            print(f'First Name: {self.first_name}')
            print(f'Last Name: {self.last_name}')
            print(f'Email: {self.email}')
            print(f'Age: {self.age}')
            print(f'Is Reward Member: {self.is_reward_member}')
            print(f'Gold Card Points: {self.gold_card_points}')
            print('*********')
            return self

    def enroll(self):
        if self.is_reward_member == True:
            print('User already a member.')
            print('*********')
        else:
            self.is_reward_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            self.gold_card_points = 0
            print('User does not have enough points!')
        return self

robyn = User('Robyn', 'Lang', 'rtlang@oakwood.edu', 44)

robyn.display_info().enroll().spend_points(50).display_info()

monique = User('Monique', 'Morales-Mason', 'mmoralesmason@oakwood.edu', 42)

michelle = User('Michelle', 'Ramey', 'mramey@oakwood.edu', 64)

monique.enroll().spend_points(80).display_info()

michelle.display_info().spend_points(40)

robyn.enroll()