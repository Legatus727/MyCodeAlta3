#!/usr/bin/env python3
""" Tim Robbins
    Hero - Class Model """

class Hero:
    """ Hero Class for game """

    # Constructor
    def __init__(self, name) -> None:
        self.name = name
        self.health = 20
        self.attack = 2
        self.defense = 0
        self.inventory = []

    # Function to display useful stats about the Hero
    def __str__(self) -> str:
        return f"{self.name}'s Stats\n\tHealth: {self.health}\n\tAttack: {self.attack}\n\tDefense: {self.defense}\n\tInventory: {self.inventory}"

    # Add weapon strength the Hero Stats
    def addWeapon(self, strength) -> None:
        self.attack = strength

    # Add armor strength to Hero Stats
    def addArmor(self, armor) -> None:
        self.defense = armor

    # Function to process an attack on the Hero
    def receiveAttack(self, strength) -> None:

        # If attack is not greater than Hero's defense, attack has no effect
        if (strength <= self.defense):
            print('Attack was ineffective')
        else:
            healthHit = strength - self.defense
            print('Attack breached defenses!')
            print(f'Received {healthHit} damage!')

            self.health -= healthHit

            if (self.health <= 0):
                self.heroicDeath()

    # Add inventory to Hero
    def addInventory(self, type) -> None:
        self.inventory.append(type)

    # Notify Player that Hero has died
    def heroicDeath(self) -> None:
        print(f'{self.name} has perished')
