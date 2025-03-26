# --- Player, Character, Clss

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.health = 100
        self.attack_power = 10
        self.defense = 10

    def setHealth(self, health):
        self.heath = health

    def attack(self):
        print('Attack!')
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f'{self.name} is dead')

class PlayerCharacter(Character):
    def __init__(self, name, character_class, player):
        super().__init__(name, character_class)
        self.player = player
        self.inventry = []

class NpcCharacter(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.droplist = []

class CharacterClass:
    def __init__(self, className):
        self.className = className

    def setupCharacter(character):
        print('Abstract class no function')

class WarriorClass(CharacterClass):
    def __init__(self):
        super().__init__('Warrior')

    def setupCharacter(character):
        character.health += 100

class MagicianClass(CharacterClass):
    def __init__(self):
        super().__init__('Magician')

c1 = NpcCharacter('Hors', WarriorClass())
p1 = PlayerCharacter('Hansli', 'MagicianClass', 'Player1')

print(c1.health)