from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

""" BONUS Tasks I have implented: 
        - I have completed all the "Optional Challenges" in the assignment
        - Also, made "password" only accept alphanumerical characters
        - made "Donation" dollar amounts rounded to 2 decimal places

"""
# TASK 2 - Show homepage and initialize app data
database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

# TASK 3 - Handle user input
# TASK 4 - Login Functionality
    prompt = input("Please choose an option: ")
    if prompt == "1":
        username = input("Username: ").lower() #BONUS, username is incasesensitive
        password = input("Password: ").lower() #BONUS, password is incasesensitive
        authorized_user = login(database, username, password)

# TASK 5 - Register Functionality
    elif prompt == "2":
        username = input("Please enter username: ").lower() #BONUS, username is incasesensitive
        if not username[0].isalpha():                       #BONUS, username only accepts alphanumeric characters
            print("\nUsername must begin with A-Z")         
        elif not username.isalnum():
            print("\nUsername must only contain alphanumeric characters.")  
        else:
            password = input("Please choose a password: ").lower() #BONUS, password is incasesensitive
            if not password.isalnum():  #BONUS, site logic: password only accepts alphanumeric characters
                print("\nPassword must only contain alphanumeric characters.")  
            else:
                authorized_user = register(database, username, password)
                if authorized_user != "":
                    database[username] = password        

# TASK 6 - Donation Functionality
    elif prompt == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
            print(f"UPDATED DONATION LIST: {donations}")

# TASK 7 - Show Donations Functionality
    elif prompt == "4":
        show_donations(donations)

    elif prompt == "5":
        print("\nLeaving DonateME...")
        exit()

