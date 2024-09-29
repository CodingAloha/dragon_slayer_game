import random

high_score = 0


def dice_game():
    while True: 
        global high_score 
        roll_1, roll_2 = random.randint(1,6), random.randint(1,6)
        new_score = roll_1 + roll_2

        print("Current High Score: ",high_score)
        print("1) Roll Dice\n2) Leave Game")
        option = input("Enter your choice: ")

        if option == "2":
            print("Goodbye!")
            exit()
        elif option == "1":
            print("\nYou roll a...",roll_1)
            print("You roll a...",roll_2)
            if new_score > high_score:
                high_score = new_score
                print("\nNew High Score!\n")
        else:
            print("Error, must choose 1 or 2") 

dice_game()
