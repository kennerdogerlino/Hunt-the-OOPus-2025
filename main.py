"""Imports cave to Area"""
import os
from area import Area
from character import Enemy

def clear_console():
    """Clears the console in terminal"""
    os.system("cls" if os.name == "nt" else "clear")

#Spawnpoint (can respawn when dead)
Wooden_house = Area("Wooden House")

#Level 1 forest biome section
Forest_entrance = Area("forest entrance")
Giant_Tree = Area("Giant Tree")
Platforms = Area("Platforms")
Abandoned_Room  = Area("Abandoned room")

#Level 2 Jungle Biome section
Jungle_Biome_entrance = Area("Wooden House")
Jungle_ravine = Area("Wooden House")
#South/down direction from jungle ravine
Vine_covered_wall = Area("Wooden House")
GOLDEN_CHEST = Area("Wooden House")
Golden_chest = Area("Wooden House")
#West direction going past ravine
Rainforest = Area("Wooden House")

#Level 3 Hallowed Biome section
Hallowed_Biome_entrance

#Link_areas
Wooden_house.link_areas()

chocolate10992 = Enemy("chocolate10992", "A dirty, smelly Bot")
chocolate10992.set_conversation("Come closer little one. I cannot see you.")
chocolate10992.set_weakness("touching grass")
Wooden_house.set_character(chocolate10992)


current_area = Wooden_house
DEAD = False
while DEAD is not False:
    print("\n")
    current_area.get_details()
    inhabitated = current_area.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_area = current_area.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What you fight with cuh? ")
            if inhabitated.fight(fight_with) is True:
                print("W's in the chat! You win the battle")
            else:
                print("Flabbergastinations! You lost the fight.")
                DEAD = True
        else:
            print("There is no one here to fight with")
