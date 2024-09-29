# TASK 1 Set up Files and Folders
def show_homepage():
    print("""\n                       === DonateMe Homepage ===           
            --------------------------------------------
            | 1.    Login       | 2.    Register        |
            --------------------------------------------
            | 3.    Donate      | 4.    Show Donations  |
            --------------------------------------------
            |               5. Exit                     |
            --------------------------------------------""")

# TASK 6 - Donate Functionality
def donate(username):
    donation_amt = float(input("\nEnter amount to donate: $"))
    donation = username + " donated $" + str(round(donation_amt, 2))    #BONUS, site logic: donation amount rounded to 2 decimal places
    print("Thank you for your donation!")
    return donation

# TASK 7 - Show Donations Functionality
def show_donations(donations):
    total = 0
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
            idx = donation.find('$') + 1     
            total += float(donation[idx:])   
    print(f"\nTotal donations: ${str(total)}") # BONUS, display "Total Donations"