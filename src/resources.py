


class Character:

    def __init__(self, name, health, attack, armor):
        self.name=name
        self.health=health
        self.attack=attack
        self.armor=armor

    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"

class Goblin:

    def __init__(self,  health, attack, armor):
        self.health=health
        self.attack=attack
        self.armor=armor

    def __str__(self) -> str:
        return f"Goblin: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"