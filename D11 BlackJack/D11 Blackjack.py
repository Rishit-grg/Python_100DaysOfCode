import random as rnd

balance = 100
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
rounds_won =0 

# Round
while balance > 0 :

    print(f"You currently have a balance of {balance}$")

    # Deal amount input
    while True:
        deal = int(input("How many $ do you want to deal ? - "))
        if deal <= balance:
            if deal == balance:
                print("All Right...ALL IN")
            balance = balance - deal
            break
        else:
            print("Insufficient Balance. Enter again ")


    # Inital cards dealing
    print("\nShuffling Deck.....\nDealing cards.....")
    dealer_cards = [rnd.choice(deck)]
    print("Dealer's cards - ", dealer_cards)
    player_cards = [rnd.choice(deck), rnd.choice(deck)]
    print("Your cards are - ", player_cards)


    # Hit or Stand
    while True:
        move = (input("Do you want to Hit (H) or Stand (S)? - ")).lower().strip()
        if move and move[0] == "h" and sum(player_cards) < 21:
            player_cards.append(rnd.choice(deck))
            print("Your cards are - ", player_cards)

            while sum(player_cards) > 21:
                if 11 in player_cards:
                    player_cards[player_cards.index(11)] = 1
                    print("Saved Bust - Your ace changed to 1")
                    print("Your cards are - ", player_cards)
                    continue
                break
        elif move and move[0] == "h" and sum(player_cards) >= 21:
            print("Over the limit, Cannot hit anymore ")
            break
        elif move == "s":
            break
        else:
            print("Invalid Input ")


    # Dealer hand
    if sum(player_cards) <= 21:

        while sum(dealer_cards) < 17:
            dealer_cards.append(rnd.choice(deck))

            while sum(dealer_cards) > 21:
                if 11 in dealer_cards:
                    dealer_cards[dealer_cards.index(11)] = 1
                    print("(Dealers changes ace 11 to 1)")
                    continue
                break
        print("Dealer's cards are - ", dealer_cards)

    # Result decision
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    print(f"Your sum is {player_sum}\nThe dealers sum is {dealer_sum}")

    if player_sum == dealer_sum:
        print("Draw")
        balance = balance + deal
    elif dealer_sum == 21:
        if len(dealer_cards) == 2:
            print("DEALER'S BLACKJACK : You lose this round ")
        else :
            print("You lose this round ")
    elif player_sum == 21:
        if len(player_cards) == 2:
            print("BLACKJACK : You win this round ")
            balance += int(2.5 * deal)
        else :
            print("You win this round ")
            balance += int(2 * deal)
    elif player_sum > 21:
        print("Busted : You lose this round ")
    elif dealer_sum > 21:
        print("Dealer Busted : You win this round ")
        balance += (2 * deal)
    elif player_sum > dealer_sum:
        print("You win ")
        balance += (2 * deal)
    else:
        print("You lose ")

    # Play more ?
    want_to_cashout = (input("Do you want to play further (enter) or CashOut(C)")).lower().strip()
    if want_to_cashout and want_to_cashout[0] == "c":
        break
    print("-"*50 + "\n")

# Cashout
if balance == 0:
    print("You are out of balance")

print(f"CASHOUT - {balance}$")

# Stats


# TODO 
# input validations 
# print stats with cashout
# make showing A K Q J possible
# make another file database for keeping records of all players who ever played this and high scores
