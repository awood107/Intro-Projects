import random

# Creates the cards in a deck, future
num_decks = 2
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
face_cards = ["J", "Q", "K"]
ten_cards = ["J", "Q", "K", "10"]

# Defines a function to get the numerical value of the card, currently no support for Ace to be 1 or 11
def get_value(card):
    if card in face_cards:
        return 10
    elif card == "A":
        return 11
    else:
        return int(card)

# Defines a function to draw a card
def draw_card():
    card = play_deck[random.randint(0, card_count)]
    return card

# Initializes the play deck and creates variables for deck information
play_deck = deck * int(num_decks)
num_cards = len(play_deck)
card_count = num_cards - 1

# Area for future feature of placing wager
cash = 100

# Initializes the dealers hand and returns the dealers first card
dealer1 = draw_card()
dealer2 = draw_card()
dealer_value1 = (get_value(dealer1))
dealer_value2 = (get_value(dealer2))
dealer_sum = (dealer_value1 + dealer_value2)
dealer_hand = [dealer_value1, dealer_value2]
print(dealer1)

# Initializes the players hand and returns the players hand along with the numerical value
player1 = draw_card()
player2 = draw_card()
player_value1 = (get_value(player1))
player_value2 = (get_value(player2))
player_sum2 = (player_value1 + player_value2)
player_hand = [player_value1, player_value2]
print(player1 + " " + player2 + "     " + str(player_sum2))

dealer_blackjack = False
player_blackjack = False

# This section checks if either player was dealt blackjack, no current functionality for insurance
if dealer1 == "A" and dealer2 in ten_cards or (dealer2 == "A" and dealer1 in ten_cards):
    dealer_blackjack = True
    play = False

if player1 == "A" and player2 in ten_cards or player2 == "A" and player1 in ten_cards:
    player_blackjack = True
    play = False

if dealer_blackjack:
    if player_blackjack:
        print("Push, you both got Blackjack")
    else:
        print("Dealer got Blackjack, you lose")
elif player_blackjack:
    if dealer_blackjack:
        print("Push, you both got Blackjack")
    else:
        print("You got Blackjack, you Win!")
else:
    play = True


player_sum = (player_value1 + player_value2)
decision = []

# Loops through the players turn until they decide to stand, need to add else statement for not supported input
if play is True:
    while player_sum < 21 and (decision == 'Hit' or decision == []):
        while decision == 'Hit' or decision == []:
            decision = input("Stand or Hit?: ")
            if decision == "Hit":
                hit = draw_card()
                player_hand.append(hit)
                player_sum += get_value(hit)
                print(player_hand)
                print(player_sum)
                if player_sum > 21:
                    print("You Lost! (Bust)")
                    play = False

# Starts the dealers turn
if play is True:
    while dealer_sum < 17:
        hit = draw_card()
        dealer_hand.append(hit)
        dealer_sum += get_value(hit)
        print(dealer_hand)
        if dealer_sum > 21:
            print("You win! Dealer bust")
            play = False

if play is True:
    if dealer_sum > player_sum:
        print("Dealer wins! The dealer had " + str(dealer_sum) + " you had " + str(player_sum))
    elif dealer_sum == player_sum:
        print("Push!")
    else:
        print("You win! The dealer had " + str(dealer_sum) + " you had " + str(player_sum))
