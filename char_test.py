"""test"""
from character import Enemy

Joyboy = Enemy("Joyboy", "A dirty, smelly Bot")
Joyboy.describe()
Joyboy.set_conversation("Come closer little one. I cannot see you.")
Joyboy.talk()
print(Joyboy)
Joyboy.set_weakness("touching grass")

fight_with = input("What you fight with cuh? ")
Joyboy.fight(fight_with)
