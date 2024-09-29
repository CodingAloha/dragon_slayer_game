import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_option = input("Enter to pick a card or Q + enter to quit: ").upper()
    if user_option == "Q":
        quit()
    else:
        random_pick = random.choice(diamonds)
        hand.append(random_pick)
        diamonds.remove(random_pick)
        print(f"Remaining cards: {diamonds}")
        print(f"Your hand: {hand}")
if not diamonds:
    print("There are no more cards to pick!!!")
