# Task 1 - Set up the Game
wizard, wizard_hp, wizard_damage = "Wizard", 70, 150
elf, elf_hp, elf_damage = "Elf", 100, 100
human, human_hp, human_damage = "Human", 150, 20
knight, knight_hp, knight_damage = "Knight", 200, 100
dragon_hp, dragon_damage = 300, 50

# Task 2 - Prompt Player    
while True:
    print("1) Wizard\n2) Elf\n3) Human\n4) Knight\n5) Exit")
    character = input("Choose your character: ").lower()
        
# Task 3 - Player Choice
    if character == "5" or character == "exit":
        print("Goodbye!")
        exit() 
        # lines 19-20 were the old code, before correction
        # exit_flag = True (I didn't know what "exit_flag" was but it was in the cheat sheet so I thought I needed it)
        # break

    if character == "1" or character == wizard.lower():
        character, my_hp, my_damage = wizard, wizard_hp, wizard_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break

    if character == "2" or character == elf.lower():
        character, my_hp, my_damage = elf, elf_hp, elf_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break

    if character == "3" or character == human.lower():
        character, my_hp, my_damage = human, human_hp, human_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break
    
    if character == "4" or character == knight.lower():
        character, my_hp, my_damage = knight, knight_hp, knight_damage
        print(f"You have chosen the character: {character}")
        print(f"Health: {my_hp}")
        print(f"Damage: {my_damage}")
        break


    else:
        print("Unknown character")
        
# Task 4 - Battle with the Dragon!
while True:

    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}")
    print("")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break

    my_hp = my_hp - dragon_damage
    print(f"The Dragon strikes back at {character}")
    print(f"The {character}'s hitpoints are now: {my_hp}")
    print("")
    if my_hp <= 0:
        print(f"The {character} has lost the battle.")
        break

while True:
    play_again = input("Play again? (y/n): ").lower()
    if play_again == "n" or play_again == "no":
    # line 78 was the old code before correction
    # if play_again == "n" or "no":
        print("Goodbye!")
    break
# I don't know how to make it so that "Y" or "Yes" restarts the game

