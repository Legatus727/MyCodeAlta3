#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)
    print(pokeapi["sprites"]["front_default"])
    for x in pokeapi["moves"]:
        print(x["move"]["name"])
    print(len(pokeapi["game_indices"]))
main()

