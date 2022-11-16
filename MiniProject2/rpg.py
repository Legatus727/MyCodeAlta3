#!/usr/bin/env python3
"""Driving a simple console rpg game | Tim Robbins, Alta3 Research"""

from Hero import Hero
from Monster import Monster, AlphaMonster, Dragon
from os import system, name
from time import sleep

def showInstructions() -> None:
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      attack [monster]
      flee [direction]
    ========
    Objective:
      Find the key to exit the castle!

      Find and defeat the dragon to save the Kings favourite Thanksgiving Pie!
      Beware of monsters that have overrun the castle!

      * Hint *: Finding weapons / armor will greatly improve your chances!

    Press Enter to Continue:
    ''')

def showStatus(hero, map, currentRoom) -> None:
    """determine the current status of the player"""

    # print Hero stats
    print(hero)

    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)

    # check if there's an item in the room, if so print it
    if "item" in map[currentRoom]:
      print('You see a ' + map[currentRoom]['item'])
    print("---------------------------")

def clear() -> None:
    """Clear the terminal"""

    # for windows
    if name == 'nt':
        system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

def combat(monster, hero) -> None:
    """ Driver Function for combat """

    clear()
    print('Entering Combat.....')
    sleep(3)

    # Loop through attack sequences until finished
    while (monster.health > 0 and hero.health > 0):
        # Display Stats
        clear()
        print(monster)
        print('===========')
        print(hero)

        # Process Attacks
        sleep(2)
        print('Hero attacking!')
        monster.receiveAttack(hero.attack)
        sleep(2)
        print(f'{monster.name} attacking!')
        hero.receiveAttack(monster.attack)
        sleep(2)

    # Display Combat Results
    if (monster.health <= 0):
        print(f'{monster.name} has been defeated. Well Done!')
        sleep(2)
    if (hero.health <= 0):
        print('The Hero has perished!')
        sleep(2)

def displayMoveOptions(map, currentRoom) -> None:
    print('You look around and must decide a course to follow..')
    for key, value in map[currentRoom].items():
        if (key != 'item'):
            print(f'{key} : {value}')
    print("---------------------------")

def main():
    """Driver for game, called at run time"""
    # a dictionary linking a room to other rooms
    map = {   
        'Hall' : {
            'south' : 'Kitchen',
            'east'  : 'Entryway',
            'north' : 'Armory',
        },

        'Armory' : {
            'south' : 'Hall',
            'north' : 'Armory - Upper',
            'item'  : 'sword'
        },

        'Armory - Upper' : {
            'south' : 'Armory',
            'item'  : 'shield'
        },

        'Kitchen' : {
            'north' : 'Hall',
            'item'  : 'monster'
        },

        'Entryway' : {
            'west' : 'Hall',
            'south' : 'Garden',
            'north' : 'Attic',
            'east' : 'Courtyard',
        },
        'Garden' : {
            'north' : 'Entryway',
            'item'  : 'key'
        },
        'Attic' : {
            'south' : 'Entryway',
            'item' : 'Alpha Monster'
        },
        'Courtyard' : {
            'west' : 'Entryway',
            'north' : 'Mountain Pass',
            'east' : 'Woods'
        },
        'Woods' : {
            'west' : 'Courtyard',
            'item' : 'Alpha Monster'
        },
        'Mountain Pass' : {
            'south' : 'Courtyard',
            'north' : 'Dragon Lair'
        },
        'Dragon Lair' : {
            'item' : 'Dragon'
        }
    }

    # start the player in the Hall
    currentRoom = 'Hall'
    endGame = False

    # Show Instructions
    showInstructions()
    input()

    heroName = input("What shall you be called, Hero?\n> ")
    player = Hero(heroName)

    # breaking this while loop means the game is over
    while not endGame:
        clear()
        showStatus(player, map, currentRoom)
        displayMoveOptions(map, currentRoom)

        # the player MUST type something in
        # otherwise input will keep asking
        move = ''
        while move == '':  
            move = input('> ')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':

            #check that they are allowed wherever they want to go
            if move[1] in map[currentRoom]:
                
                # if move is to courtyard, ensure player has key to exit!
                if (map[currentRoom][move[1]] == 'Courtyard'):
                    if 'key' in player.inventory:
                        #set the current room to the new room
                        currentRoom = map[currentRoom][move[1]]
                    else:
                        # Inform player they must find the key!
                        print('The door is locked! Find the key!')
                        sleep(1)

                else:
                    #set the current room to the new room
                    currentRoom = map[currentRoom][move[1]]

            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')
                sleep(1)

        #if they type 'get' first
        if move[0] == 'get' :

            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "item" in map[currentRoom] and move[1] in map[currentRoom]['item']:

                #add the item to their inventory
                player.addInventory(move[1])

                if (move[1] == 'sword'):
                    player.attack = 8
                if (move[1] == 'shield'):
                    player.defense = 6

                #display a helpful message
                print(move[1] + ' got!')
                sleep(1)

                #delete the item key:value pair from the room's dictionary
                del map[currentRoom]['item']

            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
                sleep(1)

        ## If a player enters a room with a monster
        if 'item' in map[currentRoom]:
            if 'monster' in map[currentRoom]['item']:
                print('A monster is before you.. attack or flee!')

                # Create new monster for room and show stats
                monster = Monster()
                print(monster)

                # Determine if player wants to attack or flee
                response = input('> ')
                response = response.lower().split(" ", 1)

                if (response[0] == 'attack'):
                    # Combat with Monster
                    combat(monster, player)
                    if (player.health <= 0):
                        endGame = True
                else:
                    #check that they are allowed wherever they want to go
                    if move[1] in map[currentRoom]:

                        #set the current room to the new room
                        currentRoom = map[currentRoom][move[1]]

                    # if they aren't allowed to go that way:
                    else:
                        print('You can\'t go that way!')
                        combat(monster, player)
                        if (player.health <= 0):
                            endGame = True
            elif 'Alpha Monster' in map[currentRoom]['item']:
                print('A Alpha Monster is before you!!! Attack or FLEE!')

                # Create new monster for room and show stats
                monster = AlphaMonster()
                print(monster)

                # Determine if player wants to attack or flee
                response = input('> ')
                response = response.lower().split(" ", 1)

                if (response[0] == 'attack'):
                    # Combat with Monster
                    combat(monster, player)
                    if (player.health <= 0):
                        endGame = True
                else:
                    #check that they are allowed wherever they want to go
                    if response[1] in map[currentRoom]:

                        #set the current room to the new room
                        currentRoom = map[currentRoom][response[1]]

                    # if they aren't allowed to go that way:
                    else:
                        print('You can\'t go that way!')
                        sleep(1)
                        combat(monster, player)
                        if (player.health <= 0):
                            endGame = True
            elif 'Dragon' in map[currentRoom]['item']:
                print('The dragon has appeared before you! Attack! For the King\'s pie!!!')

                # Create Dragon and initiate combat
                sleep(2)
                dragon = Dragon()
                combat(dragon, player)

                if (player.health <= 0):
                    endGame = True
                else:
                    print('You have saved the pie! Well Done!')
                    endGame = True

if __name__ == '__main__':
    main()
