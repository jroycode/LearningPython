
class ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        pet.noise()


class pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy = self.energy + 25
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.heath = self.health + 10
        return self

    def play(self):
        self.health = self.heath + 5
        return self

    def noise():
        print("AWOOOOOOO")

baker = pet("Baker", "Golden-Doodle", "Knuckles", 100,1000)
mia = pet("Mia", "Husky", "Shake",100,100)

josh = ninja("Joshua", "Roy", "Chicken", "Blue Buffalo", baker)
hannah = ninja("Hannah", "Roy", "Sausage", "Call of the Wild", mia)

josh.feed()
josh.walk()
josh.bathe()