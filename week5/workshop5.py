import random
# Task 1
def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)

    while tries != 0:
        print(f"Guesses remaining: {tries}")
        guess = int(input("Guess a number: ")) # BONUS - only accepts integers
        if guess == random_number:
            print("You guessed correct!")
            return None
        elif guess != random_number:
            if guess < random_number:
                print("Guess higher!")
            elif guess > random_number:
                print("Guess lower!")
            tries -= 1
        if tries == 0:
            print("You have run out of guesses :(")

# Task 2
def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"Target number : {random_number}")
    for value in range(start, stop+1):
        if tries == 0:
            print("Computer has run out of guesses!")
            win = False
            return win
        if value == random_number:
            print("Computer guessed correct!")
            win = True
            return win
        else:
            print(f"Computer guessed: {value}")
            print(f"Guess remaining: {tries}")
            tries -= True
        
# Task 3
def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    print(f"Target number: {random_number}")
    print(f"Guesses remaining: {tries}")

    while tries:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_number:
            print("You guessed correct!")
            return None
        elif pivot > random_number:
            upper_bound = pivot - 1
            print(f"Your guess: {pivot}")
            print("Guess higher!")
        elif pivot < random_number:
            print(f"Your guess: {pivot}")
            print("Guess lower!")
            lower_bound = pivot + 1
        tries -= 1
        print(f"Tries remaining: {tries}")

# BONUS Task - function that when asked, user inputs number of tries and number range and choose search function
def user_input():
    tries = int(input("Please enter number of tries: "))
    start = int(input("Enter starting number: "))
    stop = int(input("Enter ending number: "))
    search = input("""Which search would you like to use:
                   1. User Input Search
                   2. Linear Search
                   3. Binary Search\n""").lower()
    if search == '1' or search == "user input search":
        guess_random_number(tries, start, stop)
    elif search == '2' or search == "linear search":
        guess_random_num_linear(tries, start, stop)
    elif search == '3' or search == "binary search":
        guess_random_num_binary(tries, start, stop)

# BONUS - function for gambling game
def gambling_game():
    player_money = 10   # player starts with $10

    while player_money >= 0 or player_money >= 50:  # while loop to run the game until player balance equals $0 (lose) or $50 (win)
        if player_money <= 0:   # player loses if they reach $0
            print("You ran out of money!")
            break
        elif player_money >= 50:    # player wins if they reach $50
            print("You won the game!")
            break

        # player chooses to bet if the computer will guess correctly or incorrectly
        while True:
            bet_on_computer = int(input("""\nPlace Bet:     
        1. Computer will guess number correctly
        2. Computer will NOT guess number correctly
            Enter '1' or '2': """))
            if bet_on_computer == 1:
                bet_on_computer = True
                break
            elif bet_on_computer == 2:
                bet_on_computer = False
                break
            else:
                print("Invalid input. Enter '1' or '2'")

        # player inputs how much they would like to bet
        while True:
            print(f"\nCurrent balance: ${player_money}")    # player balance
            bet_amount = int(input("How much would you like to bet?\n"))
            if bet_amount <= player_money:  # place bet
                player_money -= bet_amount
                print(f"You bet ${bet_amount}")
                payout = bet_amount * 2
                break
            else:   # can't place bet if balance is less than bet amount
                print("Not enough funds")
            
        result = guess_random_num_linear(5, 0, 10)  # storing a variable to see if the computer guess correctly or incorrectly
        if result == True:  # if computer guessed correctly
            if bet_on_computer == True: # if player bet on computer to guess correctly
                print("\nYou won your bet, the computer guessed correctly")
                print(f"You won ${payout}")
                player_money += payout
            elif bet_on_computer == False:  # if player bet on computer to guess incorrectly
                print("\nYou lost your bet, the computer guessed correctly")
                bet_amount -= player_money
        elif result == False:   # if computer guessed incorrectly
            if bet_on_computer == False:    # if player bet on computer to guess incorrectly
                print("\nYou won your bet, the computer guessed incorrectly")
                print(f"You won ${payout}")
                player_money += payout
            elif bet_on_computer == True:   # if player bet on computer to guess correctly
                print("\nYou lost your bet, the computer guessed incorrectly")
                bet_amount -= player_money
        print(f"Current balance :${player_money}")

# BONUS Task Driver - gambling game()          
# gambling_game()

# Task 1 Driver code - guess_random_number()
# guess_random_number(5, 0, 10)

# Task 2 Driver code - guess_random_num_linear()
# guess_random_num_linear(5, 0, 10)

# Task 3 Driver code - guess_random_num_binary()
# guess_random_num_binary(5, 0, 100)

# Bonus Task Driver code - user_input() 
# user_input()
