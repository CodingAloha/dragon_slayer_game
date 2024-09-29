# TASK 4 - Login Functionality
def login(database, username, password):
    if username in database and database[username] == password:
        print(f"\nWelcome back {username}!")
        return username
    elif username in database and database[username] != password:
        print(f"\nIncorrect password for {username}.")
        return ""
    else:
        print("\nUsername not found. Please Register")
        return ""
    
# TASK 5 - Register Functionality
def register(database, username, password):
    if username in database:
        print("\nUsername already registered.")
        return ""
    if len(username) > 10: # BONUS, username musn't exceed 10 characters
        print("\nUsername must not exceed 10 characters.")
        return ""
    if len(password) < 5: # BONUS, password need at least 5 characters
        print("\nPassword must be at least 5 characters.")
        return ""

    else:
        print(f"\nUsername has been registered")
        return username
    
    
