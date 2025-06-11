"""Imports cave to Cave"""
import os
from cave import Cave
from character import Enemy

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings.")
dungeon = Cave("Dungeon")
dungeon.set_description("A Large cave with a rack.")

chocolate10992 = Enemy("chocolate10992", "A dirty, smelly Bot")
chocolate10992.set_conversation("Come closer little one. I cannot see you.")
chocolate10992.set_weakness("touching grass")
dungeon.set_character(chocolate10992)

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

current_cave = cavern
dead = False
while dead == False:
    print("\n")
    current_cave.get_details()
    inhabitated = current_cave.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_cave = current_cave.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What you fight with cuh? ")
            if inhabitated.fight(fight_with) is True:
                print("W's in the chat! You win the battle")
            else:
                print("!Blasphemy! You lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with")

    def clear_console():
        """Clears the console in terminal"""
        os.system("cls" if os.name == "nt" else "clear")
