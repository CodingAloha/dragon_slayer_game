# TASK 1
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# TASK 2
    def change_name(self, new_name):
        if not len(new_name) >= 2 and len(new_name) <= 10:  # BONUS, only allow 2-10 characters for new name
            print("Invalid name, must be 2 - 10 characters.")
        elif self.name == new_name: # BONUS, can't use same name
            print("Choose a new name.")
        elif ' ' in new_name:   # BONUS, no spaces allowed
            print("No spaces allowed.")
        else:
            self.name = new_name                            

    def change_pin(self, new_pin):
        if len(new_pin) != 4:   # BONUS, only allow 4 characters for new PIN
            print("Invalid PIN, must be 4 characters.")
        elif self.pin == new_pin:   # BONUS, can't use same PIN
            print("Choose a new PIN.")
        elif ' ' in new_pin:   # BONUS, no spaces allowed
            print("No spaces allowed.")
        else:
            self.pin = new_pin
 
    def change_password(self, new_password):
        if not len(new_password) >= 5:  # BONUS, only allow 5 or more characters for new password
            print("Invalid password, must be 5 or more characters.")
        elif self.password == new_password: # BONUS, can't use same password
            print("Choose a new password.")
        elif ' ' in new_password:   # BONUS, no spaces allowed
            print("No spaces allowed.")
        else:
            self.password = new_password
 
# TASK 3
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0   # BONUS, show 2 decimal places

# TASK 4
    def show_balance(self):
        print("{} has an account balance of: ${}".format(self.name, self.balance))

    def withdraw(self, withdraw_amount):
        if withdraw_amount < 0:     # BONUS, error if amount is a negative number or string
            print("Invalid amount, must be greater than $0")
        else:
            self.balance -= withdraw_amount

    def deposit(self, deposit_amount):
        if deposit_amount < 0:      # BONUS, error if amount is a negative number or string
            print("Invalid amount, must be greater than $0")
        else:
            self.balance += deposit_amount

# TASK 5
    def transfer_money(self, user, amount):
        if amount < 0:      # BONUS, error if amount is a negative number or string
            print("Invalid amount, must be greater than $0")
        else:
            if amount > self.balance:   #Bonus, error if user's account has less money than transfer request
                print("Insufficient funds, transaction canceled")
            else:
                print("\nYou are transferring ${} to {}".format(amount, user.name))
                print("Authentication required")
                user_pin = input("Enter your pin: ")
            
                if user_pin != self.pin:
                    print("Invalid PIN. Transaction canceled.")
                    return False
                else:
                    print("Transfer authorized")
                    self.balance -= amount
                    user.balance += amount
                    print("Transferring ${} to {}".format(amount, user.name))
                    return True
        
    def request_money(self, user, amount):
        if amount < 0:      # BONUS, error if amount is a negative number or string
            print("Invalid amount, must be greater than $0")
        else:
            if amount > user.balance:   #Bonus, error if user's account that is being request from has less than request amount   
                print("Insufficient funds, transaction canceled.")
            else:
                print("\nYou are requesting ${} from {}".format(amount, user.name))
                print("User authentication is required...")

                user_pin = input("Enter {}'s PIN: ".format(user.name))
                if user_pin != user.pin:
                    print("Invalid PIN. Transaction canceled.")
                    return False
                
                else:           
                    user_password = input("Enter your password: ")
                    if user_password != self.password:
                        print("Invalid password. Transaction canceled.")
                        return False
                    else:
                        print("Request authorized")
                        print("{} has sent ${}".format(user.name, amount))
                        user.balance -= amount
                        self.balance += amount                   

""" Driver Code for Task 1 """
# user1 = User("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)
''' Output:
            Bob 1234 password
'''

""" Driver Code for Task 2 """
# user1 = BankUser("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobboy")
# user1.change_pin("4321")
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)
''' Output:
            Bob 1234 password
            Bobboy 4321 newpassword
'''

""" Driver Code for Task 3 """
# user1 = BankUser("Bob", "1234", "password")
# print(user1.name, user1.pin, user1.password, user1.balance)
''' Output:
            Bob 1234 password 0
'''

""" Driver Code for Task 4 """
# user1 = BankUser("Bob", "1234", "password")
# user1.show_balance()
# user1.deposit(1000)
# user1.show_balance()
# user1.withdraw(500)
# user1.show_balance()
''' Output:
            Bob has an account balance of: $0
            Bob has an account balance of: $1000
            Bob has an account balance of: $500
'''

"""Driver Code for Task 5 """
# user1 = BankUser("Bob", "1234", "password")
# user2 = BankUser("Alice", "1234", "password")
# user2.deposit(5000)
# user2.show_balance()
# user1.show_balance()
# user2.transfer_money(user1, 500)
# user2.show_balance()
# user1.show_balance()
# user2.request_money(user1, 250)
# user2.show_balance()
# user1.show_balance()
''' Output:
            Alice has an account balance of: $5000
            Bob has an account balance of: $0

            You are transferring $500 to Bob
            Authentication required
            Enter your pin: 1234
            Transfer authorized
            Transferring $500 to Bob
            Alice has an account balance of: $4500
            Bob has an account balance of: $500

            You are requesting $250 from Bob
            User authentication is required...
            Enter Bob's pin: 1234
            Enter your password: password
            Request authorized
            Bob has sent $250
            Alice has an account balance of: $4750
            Bob has an account balance of: $250
'''
''' Output for money transfer if PIN is incorrect:
            Alice has an account balance of: $5000
            Bob has an account balance of: $0

            You are transferring $500 to Bob
            Authentication required
            Enter your pin: 1111
            Invalid PIN. Transaction canceled.
            Alice has an account balance of: $5000
            Bob has an account balance of: $0
'''
''' Output for money request if PIN is incorrect:
            Alice has an account balance of: $5000
            Bob has an account balance of: $0

            You are transferring $500 to Bob
            Authentication required
            Enter your pin: 1234
            Transfer authorized
            Transferring $500 to Bob
            Alice has an account balance of: $4500
            Bob has an account balance of: $500

            You are requesting $250 from Bob
            User authentication is required...
            Enter Bob's pin: 1111
            Invalid PIN. Transaction canceled.
            Alice has an account balance of: $4500
            Bob has an account balance of: $500
'''
''' Output for money request if password is incorrect:
            Alice has an account balance of: $5000
            Bob has an account balance of: $0

            You are transferring $500 to Bob
            Authentication required
            Enter your pin: 1234
            Transfer authorized
            Transferring $500 to Bob
            Alice has an account balance of: $4500
            Bob has an account balance of: $500

            You are requesting $250 from Bob
            User authentication is required...
            Enter Bob's pin: 1234
            Enter your password: incorrectpassword
            Invalid password. Transaction canceled.
            Alice has an account balance of: $4500
            Bob has an account balance of: $500
'''

""" BONUS TASKS:
            I could'nt figure out instance attribute on_hold task???
"""