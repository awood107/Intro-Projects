import random

# Creates the cards in a deck, future
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
deck = []

# Defines a function to draw a card

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


for suit in suits:
    for value in values:
        deck.append(Card(value,suit))


while len(deck) > 0:
    def draw_card():
        card = deck[random.randint(0, select_num)]
        return card
    num_cards = len(deck)
    select_num = num_cards - 1
    draw = draw_card()
    print(str(draw.value) + " of " + str(draw.suit))
    if draw.value == "3":
        print("Three is for me! Drink a Drink!")
    elif draw.value == "2":
        print("Two is for you! Give out a Drink")
    elif draw.value == "4":
        print("Four is for Whores! Ladies Drink!")
    elif draw.value == "5":
        print("Five is Vroom, Ert!")
    elif draw.value == "6":
        print("Six is Dicks! All the men drink! ")
    elif draw.value == "7":
        print("Seven Heaven! Last one to point up Drinks!")
    elif draw.value == "8":
        print("Eight, Make a Date! Every time you drink your date drinks!")
    elif draw.value == "9":
        print("Nine Rhyme! Say a word and rhyme around the circle")
    elif draw.value == "10":
        print("Ten is Categories! Pick a category and go around the circle!")
    elif draw.value == "J":
        print("Thumb Master! You are the thumb master until another J is drawn!")
    elif draw.value == "Q":
        print("Question Master! You are the question master until another Q is drawn!")
    elif draw.value == "K":
        print("Make a Rule! You get to make a rule!")
    elif draw.value == "A":
        print("Waterfall! Start drinking, the person to your left cant stop until you stop!")



    i = input("")
    if i == "":
        deck.remove(draw)
        select_num -= 1
    else:
        print("please hit enter \n")


