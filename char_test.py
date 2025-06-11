"""test"""
from character import Enemy

chocolate10992 = Enemy("chocolate10992", "A dirty, smelly Bot")
chocolate10992.describe()
chocolate10992.set_conversation("Come closer little one. I cannot see you.")
chocolate10992.talk()
print(chocolate10992)
chocolate10992.set_weakness("touching grass")

fight_with = input("What you fight with cuh? ")
chocolate10992.fight(fight_with)
