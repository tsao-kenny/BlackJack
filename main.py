#BLACKJACK

'''
What we need:

CLASSES:
Deck
    shuffle
    deal
Hand
    Player
    Dealer
        Display
        Do math
Money
    Bet
    Win
    Lose
    Push

FUNCTIONS:
Hit
Stay
Check win/bust
Check aces

'''

import random

#global game = True

suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
#ranks = ['A',2,3]


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + ' of ' + str(self.suit)


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((Card(suit, rank)))

    def __str__(self):
        self.deck_contains = ''
        #print("The deck contains: ")
        for x in self.deck:
            self.deck_contains+= '\n' + x.__str__()
        return self.deck_contains

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
        #self.deck.pop()

class Hand():

    def __init__(self):
        self.inhand = []
        self.aces = 0

    def __str__(self):
        currenthand = []
        for x in self.inhand:
            currenthand.append(x.__str__() )
        return str(currenthand)

    def hit(self, card): #take from deck.deal
        self.inhand.append(card)
        #return self.inhand


    def domath(self):
        #self.aces=0
        self.current_total = 0
        for x in self.inhand:
            self.current_total += values[str(x.rank)]
        self.check_aces()
        if self.aces == 2 and len(self.inhand) == 2:
            self.current_total -= 10
            self.aces = -1
        else:
            self.aces = 0
        return self.current_total, self.aces

    def check_aces(self):

        self.current_total_aces = 0
        for ace in self.inhand:
            if 'A of' in str(ace):
                self.aces += 1
                self.current_total_aces = self.current_total
        return self.aces, self.current_total_aces

    def print_aces(self):
        if self.aces > 0:
            print('or')
        while self.aces>0:
            self.current_total_aces -= 10
            print(f'Total = {self.current_total_aces} #of aces is {self.aces}')
            self.aces -= 1
            if self.aces>0:
                print('or')
        else:
            pass
        return self.current_total_aces

class Money():

    def __init__(self, balance):
        self.balance = balance

    def bet(self, bet_amount=0):
        self.bet_amount = bet_amount
        if bet_amount > self.balance:
            print("You don't have enough money!")
        else:
            self.balance -= self.bet_amount
        return self.balance

    def win_money(self, bet_amount):
        self.balance += self.bet_amount*2
        return self.balance


#SETUP
add_money = 0
while add_money == 0:
    try:
        add_money = int(input('How much money to start with? Enter whole number: '))
    except:
        print("Enter a whole number.")

money = Money(add_money)

#Build deck
deck=Deck()

#Initialize hands
PlayerHand=Hand()
DealerHand=Hand()

#shuffle the deck
deck.shuffle()

#Draw initial cards
PlayerHand.hit(deck.deal())
PlayerHand.hit(deck.deal())

DealerHand.hit(deck.deal())
DealerHand.hit(deck.deal())

#Show hands
print('Dealer has:\n' ,DealerHand.inhand[0])
print('You have:',  *PlayerHand.inhand, sep="\n")

#calculate totals
PlayerHand.domath()
print(f'Total = {PlayerHand.current_total}')
PlayerHand.check_aces()
PlayerHand.print_aces()
print(f"Your balance is {money.balance}")
