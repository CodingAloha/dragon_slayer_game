from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
# Task 2
print("    === Automated Teller Machine ===    ")
while True:
    name = input("Enter name to register: ")
    if len(name) > 10 or len(name) == 0:
        print("Please use 1-10 characters only")
    else:
        break   

while True:
        pin = input("Enter PIN: ")
        if len(pin) != 4:
            print("Please use only 4 characters")
        else:
            break

balance = 0
print(f"{name} has been registered with a starting balance of: {balance}")
# Task 3
while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        account.deposit(balance)
    elif option == "3":
        account.withdraw(balance)
    elif option == "4":
        account.logout(name)
    break

