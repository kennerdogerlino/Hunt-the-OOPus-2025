"""Character class for Hunt the OOPus"""
class Character:
    """Defines attributes and methods for Character objects"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""    
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Gives the characters a description"""
        print(self.name + " has returned!")
        print(self.description)

    def set_conversation(self, conversation):
        """Sets what the character can say"""

    def talk(self):
        """Allows characters to talk to player"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " does not want to talk to you.")

    def fight(self):
        """Allows characters to fight with the player"""
        print(self.name + " doe not want to fight with you.")
        return True
