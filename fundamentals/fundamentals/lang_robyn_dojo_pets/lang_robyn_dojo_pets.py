class ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(pet):
        print("I'm walking my pet!")

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(pet):
        print("I'm feeding my pet.")

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(pet):
        print("Time to bathe my pet!")


class pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep():
        energy += 25

    # eat() - increases the pet's energy by 5 & health by 10
    def eat():
        energy += 5
        health += 10

    # play() - increases the pet's health by 5
    def play():
        health += 5

    # noise() - prints out the pet's sound
    def noise():
        if pet() == "dog":
            print("Woof woof!")
        elif pet() == "cat":
            print("Meeoooowwwww")
        else:
            print("howdy doody!")

robyn = ninja("Robyn", "Lang", "cookies", "keebler", pet("peka", "dog", "stand on one leg", 100, 100))

robyn.walk()
robyn.feed()
robyn.bathe()

print(f"Oh no, I'm running out of {robyn.pet.name}'s {robyn.pet_food}!")

