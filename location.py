import random, enemy

descriptions = ["Hallow", "Quiet", "Whistling", "Mesmerizing", "Shrek's", "Bennett's", "Dank", "Warner's"]
location_types = ["Forest", "River", "Cave", "Fields", "Swamp", "Desert", "Tundra", "Mountains", "Valley", "River Valley", "House"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
