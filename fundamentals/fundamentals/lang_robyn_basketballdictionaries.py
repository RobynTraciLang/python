players = [
    {
        "name": "Kevin Durant",
        "age":34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age":24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age":32,
        "position": "point guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age":33,
        "position": "point guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age":32,
        "position": "power foward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "Michael Jordan",
        "age":21,
        "position": "shooting guard, small forward, outfielder",
        "team": "Chicago Bulls"
    }
]

# Challenge 1
player_instances = []

class create_player_instance:

    team_list = []

    def __init__(self, player_information):
        self.name = player_information['name']
        self.age = player_information['age']
        self.position = player_information['position']
        self.team = player_information['team']

    @classmethod
    def get_team(cls, team_list):
        for team in team_list:
            team_list.append(create_player_instance(team))

for player_information in players:
    player = create_player_instance(player_information)
    player_instances.append(player)
    # print(f"Player name: {player.name}\n,{player.age}\n,{player.position}\n,{player.team}")
    print(f"Player name: {player.name}")
    print(f"Player age: {player.age}")
    print(f"Player position: {player.position}")
    print(f"Player team: {player.team}")
    print('')

# print(player_instances)
print("********************end Challenge 1********************")
print('')

# Challenge 2
class create_player_instance2:
    def __init__(self, player_information2):
        self.name = player_information2['name']
        self.age = player_information2['age']
        self.position = player_information2['position']
        self.team = player_information2['team']

kevin = {
        "name": "Kevin Durant",
        "age":34,
        "position": "small forward",
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum",
        "age":24,
        "position": "small forward",
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving",
        "age":32,
        "position": "point guard",
        "team": "Brooklyn Nets"
}

player_instances2 = []

# Create your Player instances here!
player_kevin = create_player_instance2(kevin)
player_instances2.append(player_kevin)
print(f"Player name: {player_kevin.name}")
print(f"Player age: {player_kevin.age}")
print(f"Player position: {player_kevin.position}")
print(f"Player team: {player_kevin.team}")
print('')

player_jason = create_player_instance2(jason)
player_instances2.append(player_jason)
print(f"Player name: {player_jason.name}")
print(f"Player age: {player_jason.age}")
print(f"Player position: {player_jason.position}")
print(f"Player team: {player_jason.team}")
print('')

player_kyrie = create_player_instance2(kyrie)
player_instances2.append(player_kyrie)
print(f"Player name: {player_kyrie.name}")
print(f"Player age: {player_kyrie.age}")
print(f"Player position: {player_kyrie.position}")
print(f"Player team: {player_kyrie.team}")
print('')

print("********************end Challenge 2********************")
print('')

# Challenge 3
# ... (class definition and large list of players here)
players = [
    {
        "name": "Kevin Durant",
        "age":34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age":24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age":32,
        "position": "point guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age":33,
        "position": "point guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age":32,
        "position": "power foward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "Michael Jordan",
        "age":21,
        "position": "shooting guard, small forward, outfielder",
        "team": "Chicago Bulls"
    }
]

new_team = []
# Write your for loop here to populate the new_team variable with Player objects.
for i in players:
    new_team.append(create_player_instance(i))

print(new_team)

print('')

print(new_team[0].name)
# remember to use dot notation for accessing objects in python!
print('')

print("********************end Challenge 3********************")
print('')


# Ninja Bonus (Can't figure this out!)
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!
# for player_information in players:
#     create_player_instance.get_team(player_information)

print("********************end Ninja Bonus********************")
print('')