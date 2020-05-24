"""
Blackjack - Assignment 5

To play run "python .\\assignment_5_james_berryman.py" from the directory the file
is housed.
"""
#Importing the libraries required to run this script
import random
import os

#Declaring the variables used in the script
dealer_cards = []
user_cards = []
hit_or_stand = "h"
start_game = True

#Append random cards to users hand/list
def user_random_card(first_card=1, last_card=10):
    user_cards.append(random.randint(first_card, last_card))

#Append random cards to dealers hand/list
def dealer_random_card(first_card=1, last_card=10):
    dealer_cards.append(random.randint(first_card, last_card))

#clearing the screen before the start of a new game
os.system("cls")
#printing the opening statement
print("Welcome to Blackjack.")
print("-" * 75)
#asking the player if they wish to start a new game
#if they player inputs a y, then two random cards are appended to both hands
#if the input is a n, the script exits
while start_game:
    play = input("Do you wish to start a new game? (y/n)").lower()
    if play == "y":
        while len(user_cards) != 2:
            user_random_card()
        while len(dealer_cards) != 2:
            dealer_random_card()
            start_game = False
    elif play == "n":
        print("Game over!")
        exit()
#Printing the initial hand dealt for the user and dealer
print(f"You draw a {user_cards[0]} and a {user_cards[1]}. Your total is {sum(user_cards)}")
print(f"The dealer drew {dealer_cards[0]} and a hidden card.")

#The user will be prompted to hit or stand here, and will continue to be asked
#unless the user chooses to stand or the sum of their cards are less than 21
#If the user hits a card is appended to their hand and the sum is totaled
while hit_or_stand != "s" and sum(user_cards) < 21:
    hit_or_stand = input("Hit or stand? (h/s): ").lower()
    if hit_or_stand == "h":
        user_random_card()
        print(f"Hit! You draw a {user_cards[-1]}, your total is {sum(user_cards)}")
    elif hit_or_stand == "s":
        print("You stand")
#If the users sum goes over 21, they bust and lose the game
#If the sum is 21 a message is printed that the user stands
if sum(user_cards) > 21:
    print("Busted! The dealer wins")
    exit()
elif sum(user_cards) == 21:
    print("You Stand!")
#The dealers hidden card/total is now revealed
print(f"The dealer reveals the hidden card of {dealer_cards[1]} and has a total of {sum(dealer_cards)}")
#The dealer will now continue to hit while the sum is less than the users hand
#or the the sum is less than 17
while sum(dealer_cards) < sum(user_cards) or sum(dealer_cards) < 17:
    dealer_random_card()
    print(f"Hit! The dealer draws a {dealer_cards[-1]}, the dealers total is {sum(dealer_cards)}")
#The sum of the user and dealer are both displayed/compared
print(f"Your total is {sum(user_cards)} and the dealers total is {sum(dealer_cards)}")
#If the sum of the dealers cards has surpassed 21, they bust and the user wins
#If the sum of the user cards are greater than the dealers, the user wins
if sum(dealer_cards) > 21:
    print("The dealer has busted! You win!")
elif sum(user_cards) > sum(dealer_cards) and sum(user_cards) < 21:
    print("You win!")
#In all other scenerios (the cards are equal), the dealer wins
else:
    print("The dealer wins!")
