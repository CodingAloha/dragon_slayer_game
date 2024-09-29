import random

class Hero:
    """Hero Class with attributes: name, hp and damage"""
    def __init__(self, name, hp, damage):
       self.name = name
       self.hp = hp
       self.damage = damage

class Dragon:
    """Dragon Class with attributes: hp and damage"""
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

class Weapon:
    """Weapon Class with attributes: name and damage increases"""
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Armor:
    """Armor class with attributes: name and hp increases"""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# Hero instances
heroes = {
     "knight": Hero("Knight", 150, 50),
     "mage": Hero("Mage", 100, 100),
     "archer": Hero("Archer", 50, 150)
} 

# user's attack function
def user_strike(hero, dragon):
    """handles the user's attack on the dragon""" 
    while True:
        attack = random.randint(20, hero.damage) # uses Hero's damage stat
        swing = input("\nPress 'A' to attack\n").lower()
        if swing != "a":
            print("\nInvalid input. Press 'A' to attack!")
        else:
            print(f"\nYou strike a blow for {attack} damage")
            dragon.hp -= attack
            if dragon.hp <= 0:
                dragon.hp = 0
            print(f"Hero's remaining HP: {hero.hp}\nDragon's remaining HP: {dragon.hp}")
            break

# dragon's attack function
def dragon_strike(hero, dragon):
    """handles dragon's attack on user"""
    dragon_attack = random.randint(10, dragon.damage)
    defense = input("\nPress 'D' to attempt to defend the Dragon's attack\n").lower()
    if defense == "d":
        print(f"\nYou defend! But the Dragon still lands a blow for {dragon_attack} damage!")
        hero.hp -= dragon_attack
    else:
        print(f"\nYou failed to defend! The Dragon lands a stronger attack for {dragon_attack + 10} damage!")
        hero.hp -= (dragon_attack + 10)

    if hero.hp <= 0:
         hero.hp = 0

    print(f"Hero's remaining HP: {hero.hp}\nDragon's remaining HP: {dragon.hp}")

# Helper functions
def select_hero():
    """prompts the user to select a hero"""
    while True:
        choice = input("Please choose which background training your Hero has:\n1. Knight\n2. Mage\n3. Archer\n").lower()
        if choice == "1" or choice == "knight":
            return heroes["knight"]
        elif choice == "2" or choice == "mage":
            return heroes["mage"]
        elif choice == "3" or choice == "archer":
            return heroes["archer"]
        else:
            print("Invalid choice, please select again.")

# weapon selection function
def select_weapon(hero, currency):
    """prompts user to select weapon based on their hero and available currency"""
    while True:
        if hero.name == "Knight":
            weapon_choice = input("""Please select a worthy Weapon:
    1. $500 - Excalibur Longsword - +50 damage
    2. $700 - Leonidas' Spear - +75 damage
    3. $900 - Legolas' Dual Swords - +100 damage\n""").lower()
        elif hero.name == "Mage":
            weapon_choice = input("""Please select a worthy Weapon:
    1. $500 - Staff of Aero - +50 damage
    2. $700 - Staff of Poseidon - +75 damage
    3. $900 - Staff of Pele - +100 damage\n""").lower()
        elif hero.name == "Archer":
            weapon_choice = input("""Please select a worthy Weapon:
    1. $500 - Hawkeye's Short Bow - +50 damage
    2. $700 - Rapid Fire Cross Bow - +75 damage
    3. $900 - Samurai Longbow - +100 damage\n""").lower()

        if weapon_choice == "1" and currency >= 500:
            weapon = Weapon("Excalibur Longsword" if hero.name == "Knight" else "Staff of Aero" if hero.name == "Mage" else "Hawkeye's Short Bow", 50)
            hero.damage += 50
            return weapon, currency - 500
        elif weapon_choice == "2" and currency >= 700:
            weapon = Weapon("Leonidas' Spear" if hero.name == "Knight" else "Staff of Poseidon" if hero.name == "Mage" else "Rapid Fire Cross Bow", 75)
            hero.damage += 75
            return weapon, currency - 700
        elif weapon_choice == "3" and currency >= 900:
            weapon = Weapon("Legolas' Dual Swords" if hero.name == "Knight" else "Staff of Pele" if hero.name == "Mage" else "Samurai Longbow", 100)
            hero.damage += 100
            return weapon, currency - 900
        else:
            print("\nNot enough currency or invalid option! Please choose again.")

# armor selection function
def select_armor(hero, currency):
    """prompts user to select armor based on hero and available currency"""
    while True:
        armor_choice = input("""Please select a piece of armor:
    1. $500 - Cloak of Agility - +50 HP
    2. $700 - Helm of Strength - +75 HP
    3. $900 - Chestplate of Invincibility - +100 HP\n""").lower()

        if armor_choice == "1" and currency >= 500:
            armor = Armor("Cloak of Agility", 50)
            hero.hp += 50
            return armor, currency - 500
        elif armor_choice == "2" and currency >= 700:
            armor = Armor("Helm of Strength", 75)
            hero.hp += 75
            return armor, currency - 700
        elif armor_choice == "3" and currency >= 900:
            armor = Armor("Chestplate of Invincibility", 100)
            hero.hp += 100
            return armor, currency - 900
        else:
            print("\nNot enough currency or invalid option! Please choose again.")

def start_game():
    """main game function to intialize game and handle flow"""
    print("----- DRAGON SLAYER -----")
    print("A dragon is terrorizing the village, and only a hero can defeat it.\n")

    hero = select_hero()
    print(f"---Hero Selected: {hero.name} --- HP: {hero.hp} --- Damage: {hero.damage}")

    # Initial currency fate
    input("\nLet's see what fate has in store for your Hero: press 'Enter'")
    currency = random.randrange(500, 1000, 100)
    print(f"\nFate has granted you ${currency} to aid you in your quest.")

    # Weapon selection
    weapon, currency = select_weapon(hero, currency)
    print(f"\n{weapon.name} will accompany you into battle!")

    # Armor selection
    input("\nPress 'Enter' to receive another fortune for armor currency...")
    currency += random.randrange(500, 1000, 100)
    print(f"\nFate has granted you additional currency! Total currency: ${currency}")

    armor, currency = select_armor(hero, currency)
    print(f"\n{armor.name} will protect you in battle!")

    # Dragon encounter
    print("\nYou hunt down the Dragon and managed to sneak up for an attack to start the battle!")
    dragon = Dragon(300, 50)

    while hero.hp > 0 and dragon.hp > 0:
        user_strike(hero, dragon)
        if dragon.hp > 0:
            dragon_strike(hero, dragon)

    if hero.hp <= 0:
        print("\nYou have fallen! The dragon prevails.")
    else:
        print("\nVictory! You have slain the dragon!")

# start the game
if __name__ == "__main__":
    start_game()