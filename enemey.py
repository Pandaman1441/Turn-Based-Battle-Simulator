
# basic enemy template, user doesn't have access to these and they have their own values like exp dropped and targeting logic
class Enemey:

    def __init__(self, T):
        if T == "1":
            self.name = "Goblin"
            self.hp = 6
            self.ad = 3
            self.ap = 1
        elif T == "2":
            self.name = "Orc"
            self.hp = 10
            self.ad = 5
            self.ap = 1
        self.critChance = 0
    