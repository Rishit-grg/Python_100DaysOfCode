bids = {
    "Nobody": 0,
}

def name_validation(name_raw, bids):
    """
    Takes the name entered by the user as a string and checks if it is in an acceptable format.
    If it is'nt mentions the problem in the format and asks the user to re-input the name till it is in proper format.
    """
    while True:
        name = name_raw.strip().title()

        if len(name) == 0:
            print("Name cannot be empty.")
        elif name in bids:
            print("Name already exists, choose a different name.")
        else:
            return name

        name_raw = input("Enter name/username again - ")

def result(bids):
    """    
    Takes the dictionary of the bids entered by the users and announces the winner. 
    (If more than one person makes the winning bid, the person who bid first wins.)
    """
    print(".....RESULT.....")

    max_bid = max(bids.values())

    for name, bid in bids.items():
        if bid == max_bid:
            print((f"{name} IS THE WINNER WITH A BID OF {bid} RS.").upper())
            break

bidders_left = True
while bidders_left :
    # input name and validate 
    name_raw = input("Enter your name/useername - ")
    name = name_validation(name_raw, bids)

    # input bid amt and validate
    bid = input("Enter the bidding amount in INR - ")
    while not (bid.isdigit()):
        print("Please enter a valid number - ", end="")
        bid = input()

    # add in dictionary of bids
    bids[name] = int(bid)
    print("Your bid has been entered")

    # any more bidders
    while bidders_left:
        more_bidders = (input("Are there any more bidders ? (Y/N)")).upper().strip()

        if more_bidders == "Y":
            print("\n" * 50)
            break
        elif more_bidders == "N":
            bidders_left = False
            result(bids)
        else:
            print("Invalid input \nPlease enter Y for yes and N for No.")

# TODO introduce a rebidding fot the winners function to deal with the situation if 2 people have bid the winning amount 
