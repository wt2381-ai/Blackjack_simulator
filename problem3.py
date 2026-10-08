#/usr/bin/python
# -*- coding: utf-8 -*-
import random

suit = ['♠','♣','♦','♥']
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

class Card(object):  
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank  

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class CardCollection(object): 

    def __init__(self):
        self.cards = []

    def add_card(self, card): 
        self.cards.append(card)

    def draw_card(self): 
        self.hand = self.cards[-1]  
        self.cards.remove(self.hand)
        return self.hand

    def make_deck(self):
        self.cards = []
        for s in suit:
            for r in rank:
                self.cards.append(Card(s, r))
        random.shuffle(self.cards)

    def value(self):
        
        total = 0
        for c in self.cards:
            if c.rank == "J" or c.rank == "Q" or c.rank == "K":
                total += 10
            elif c.rank == "A":
                total += 1
            else:
                total += c.rank
        for c in self.cards:
            if c.rank == "A":
                if total <= 11:
                    total += 10
        return total


def main():
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck 

    hand = CardCollection() # your hand
    dealer = CardCollection() # dealer's hand
    
    # draw 2 cards
    i = 0
    while i < 2: 
        hand.add_card(deck.draw_card())
        i += 1
    
    print("Your cards are:", [str(card) for card in hand.cards])
    print("Your hand is:", hand.value())
    
    if hand.value() == 21:
        print("Blackjack, You win!")
        return

    choice = input("Draw or Stay? (d/s): ")
    
    while choice == "d":
        hand.add_card(deck.draw_card())
        print("Your cards are:", [str(card) for card in hand.cards])
        print("Your hand is:", hand.value())
        
        if hand.value() >= 21:
            break
        
        if len(hand.cards) == 5:
            print("5 cards, you win!")
            return
        choice = input("Draw or Stay? (d/s): ")
        
        
    if hand.value() == 21:
        print("Blackjack, You win!")
    elif hand.value() > 21:
        print("Bust, you lost!")
    else:
        while dealer.value() < 17:
            dealer.add_card(deck.draw_card())
            dealer.value()
        print("Dealer's cards are:", [str(card) for card in dealer.cards])
        print("Dealer's hand is:", dealer.value())
        
        if dealer.value() > 21:
            print("Dealer busts, you win!")
        elif dealer.value() == 21:
            print("You lost!")
        elif dealer.value() > hand.value():
            print("You lost!")
        elif dealer.value() < hand.value():
            print("You win!")
        else:
            print("Tie!")

if __name__ == "__main__":
    main()

            
