""" This module takes on an object oriented approach to a fight match
    The fighters are objects with attributes:
        name                -   str 
        health              -   int > 0
        damage_per_attack   -   int > 0
"""


class Fighter:
    """Class to create fighter objects"""
    def __init__(self, name, health, damage_per_attack):
        """Method to initiate the class objects"""
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


    def __str__(self):
        """String formatting for the class objects"""
        return f"Fighter({self.name}, {self.health}, {self.damage_per_attack})"


    def fighter_health(self):
        """ Method to warn the fighter's corner whether they can continue
            Unnecessary method but written to satisfy pylint requirements
            of a public method in the class
        """
        if self.health < 7:
            return "Fighter is almost done!"
        return "Fighter still strong enough!"


def declare_winner(fighter1, fighter2, first_attacker):
    """Battle simulation for fighters
    Args: fighter object 1, fighter object 2, str > first attacker in battle
    Returns: str > winner of the battle"""

    if fighter1.health <= 0:
        return fighter2.name
    if fighter2.health <= 0:
        return fighter1.name
    if fighter1.name == first_attacker and fighter1.health > 0 and fighter2.health > 0:
        fighter2.health -= fighter1.damage_per_attack
        return declare_winner(fighter1, fighter2, fighter2.name)
    if fighter2.name == first_attacker and fighter1.health > 0 and fighter2.health > 0:
        fighter1.health -= fighter2.damage_per_attack
        return declare_winner(fighter1, fighter2, fighter1.name)


print(declare_winner(Fighter("Lew", 20, 2), Fighter("David", 10, 5), "Lew"))
print(declare_winner(Fighter("Lew", 50, 5), Fighter("David", 30, 5), "David"))
