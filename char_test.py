"""imports character to Character"""
from character import Enemy

joyboy = Enemy("joyboy", "A dirty, smelly Bot")
joyboy.describe()
joyboy.set_conversation("Come closer little one. I cannot see you.")
joyboy.talk()
print(joyboy)
