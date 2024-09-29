# Task 4
def show_balance(balance):
    print(f"Current balance: ${str(balance)}")

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return (balance + float(amount))
    

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if float(amount) > balance:
        print("Cannot withdraw more than available balance.")
    return (balance - float(amount))
    
def logout(name):
    print(f"Goodbye {name}!")
