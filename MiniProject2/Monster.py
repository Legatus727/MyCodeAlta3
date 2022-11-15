#!/usr/bin/env python3
""" Tim Robbins
    Monster - Class
    AlphaMonster - Subclass """

class Monster:
    """ Monster class for game """

    # Constructor
    def __init__(self) -> None:
        self.name = 'Monster'
        self.health = 10
        self.attack = 3
        self.defense = 0

    # Show Stats
    def __str__(self) -> str:
        return f"{self.name}'s Stats:\n\tHealth: {self.health}\n\tAttack: {self.attack}\n\tDefense: {self.defense}"

    # Process attack received
    def receiveAttack(self, incomingAttack) -> None:
        if (incomingAttack <= self.defense):
            print("Attack had no effect!")
        else:
            print("Attack broke through defenses!")

            damage = incomingAttack - self.defense

            print(f"{self.name} has taken {damage} damage!")

            self.health -= damage

class AlphaMonster(Monster):
    """ Alpha Monster for game """
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Alpha Monster'
        self.health = 15
        self.attack = 8
        self.defense = 2

class Dragon(Monster):
    """ Dragon for game """
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Dragon'
        self.health = 20
        self.attack = 9
        self.defense = 3
