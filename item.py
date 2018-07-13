import random

class Item:
    def __init__(self, name,  healing, description):
        self.name = name
        self.healing = healing
        self.description = description

items = [
    Item("Children's Advil",  10, "You consume this and it heals you"),
    Item("Battle axe of the gods", -3, "it took away your health, why would you ever eat that?"),
    Item("Water Bottle", 5, "You Feel refreshed"),
    Item("Cross Bow", -50, "it took away your health, are you dumb?"),
    Item("MedKit", +15, "You heal all of your wounds"),
    Item("Golden Blunt", +420, "PUFF PUFF BABY!!!!"),
    Item("BITCOIN", +0, "Type BITCOIN and see what happens"),
    Item("Dagger of the Goddess", +999, "The Goddess Amara gives you strength"),
    Item("Pistol", +5, "TEE Grizzley blesses your Pistol with Pistol Play"),
    Item("Hunting Knife", +2.5, "The Hunting Knife of a past Hunter")
]

def getRandomItem():
    return random.choice(items)

def getDescription(item):
    for i in items:
        if i.name == item:
            return i.getDescription
