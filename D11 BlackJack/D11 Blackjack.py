import random as rnd

balance = 1000
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
player_bust = False
play_more = True

# Round
while balance > 0 and play_more:
    print(f"You currently have a balance of {balance}$")

    # Deal amount input
    while True:
        deal = int(input("How many $ do you want to deal ? - "))
        if deal <= balance:
            balance = balance - deal
            break
        else:
            print("Insufficient Balance. Enter again ")

    # Inital cards dealing
    print("Shuffling Deck.....\nDealing cards.....")
    dealer_cards = [rnd.choice(deck)]
    print("Dealer's cards - ", dealer_cards)
    player_cards = [rnd.choice(deck), rnd.choice(deck)]
    print("Your cards are - ", player_cards)

    # Hit or Stand
    while True:
        move = (input("Do you want to Hit (H) or Stand (S)? - ")).lower().strip()
        if move[0] == "h":
            player_cards.append(rnd.choice(deck))
            print("Your cards are - ", player_cards)
            if sum(player_cards) > 21:
                player_bust = True
                break
        elif move == "s":
            player_bust = False
            break
        else:
            player_bust = False
            print("Invalid Input ")

    # Dealer hand

    if player_bust == False:

        while sum(dealer_cards) < 17:
            dealer_cards.append(rnd.choice(deck))
        
        # ..... blackjack if dealer did not follow the 17 rule 
        # while True:
        #     if sum(dealer_cards) <= 11:
        #         dealer_cards.append(rnd.choice(deck))
        #     elif 11 < sum(dealer_cards) <= 17:
        #         if rnd.choice([True, False]):
        #             dealer_cards.append(rnd.choice(deck))
        #         break
        #     else:
        #         break

        print("Dealer's cards are - ", dealer_cards)
    else:
        dealer_cards.append(rnd.choice(deck))

    # Result decision
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    print(f"Your sum is {player_sum}\nThe dealers sum is {dealer_sum}")

    if player_bust == True:
        print("Busted : You lose this round ")
    elif player_sum == 21:
        print("BLACKJACK : You win this round ")
        balance += int(2.5 * deal)
    elif dealer_sum > 21:
        print("Dealer Busted : You win this round ")
        balance += int(2.5 * deal)
    elif dealer_sum == 21:
        print("DEALERS BLACKJACK : You lose this round ")
    elif player_sum > dealer_sum:
        print("You win this round ")
        balance += int(2.5 * deal)
    elif player_sum < dealer_sum:
        print("You lose this round ")
    elif player_sum == dealer_sum:
        print("Round draw")
        balance = balance + deal

    # Play more ?
    play_more = (input("Do you want to play further (P) or CashOut(C)")).lower().strip()
    if play_more[0] == "c":
        break

# Cashout
if balance == 0:
    print("You are out of balance")

print(f"CASHOUT - {balance}$")

# TODO 
# ace logic 
# input validations 
# print stats with cashout
# make showing A K Q J possible
# make another file database for keeping records of all players who ever played this and high scores
