
from colorama import Fore, Style
import random

from collections import Counter
from itertools import permutations
import re
colors = ["red", "green", "purple"]
shapes = ["squiggle", "oval", "diamond"]
numbers = [1, 2, 3]
fillings = ["semi", "filled", "outline"]
#The Card class
class Card:
    def __init__(self, color, shape, number, filling):
        #Display function so that it can be used to generate displaystr
        def getdisplay(color, shape, number, filling):
            returnstr = ""
            colorobj = {"red":Fore.RED, "green":Fore.GREEN, "purple":Fore.MAGENTA}
            returnstr += colorobj.get(color)
            shapeobj = {"squiggle":"~", "oval":"O", "diamond":"◊"}
            shape = shapeobj.get(shape)
            returnstr += shape * number
            fillingobj = {"semi":"▥", "filled":"█", "outline":"□"}
            returnstr += fillingobj.get(filling)
            returnstr += Style.RESET_ALL
            return returnstr
        #Initiating the variables
        self.color = color
        self.shape = shape
        self.number = number
        self.filling = filling
        self.displaystr = getdisplay(self.color, self.shape, self.number, self.filling)
    def __repr__(self):
        #display as the display string
        return self.displaystr
    def __eq__(self, value: object) -> bool:
        return self.color == value.color and self.shape == value.shape and self.number == value.number and self.filling == value.filling
    @classmethod
    def fromstr(cls, s):
        pattern = re.compile(r'(?:(\d)?([~ov])\2*([esf])([rgp]))')

        def extract_and_default(s):
            match = pattern.match(s)
            if match:
                number = match.group(1) or str(max(len(match.group(0)) - 2,1))
                symbol = match.group(2)
                color = match.group(4)
                filling = match.group(3)
                return number, symbol, color, filling
            else:
                return False
            
        mapping = {
            "r":"red",
            "g":"green",
            "p":"purple",
            "e":"outline",
            "s":"semi",
            "f":"filled",
            "~":"squiggle",
            "o":"oval",
            "v":"diamond",
        }
        if extract_and_default(s):

            number, symbol, color, filling = extract_and_default(s)

            symbol = mapping[symbol]
            color = mapping[color]
            filling = mapping[filling]
            print(color, symbol, number, filling)
            return cls(color,symbol,int(number),filling)
        return False

    def othercardtoset(self, othercard):
        #given two in a list of three, assuming that both are in the list and the list is unique, find the other value
        def other(a, b, l):
            for i in l:
                if i != a and i != b:
                    return i
        #applying other for all the attributes
        color = self.color if self.color == othercard.color else other(self.color, othercard.color, colors)
        shape = self.shape if self.shape == othercard.shape else other(self.shape, othercard.shape, shapes)
        number = self.number if self.number == othercard.number else other(self.number, othercard.number, numbers)
        filling = self.filling if self.filling == othercard.filling else other(self.filling, othercard.filling, fillings)
        #return the card class of the attributes mentioned above
        return self.__class__(color, shape, number, filling)


class CardDeck:
    def __init__(self, cards = []):
        if cards == []:
            cards = []
            #generate all possible cards, and append it to the cards list
            for color in colors:
                for shape in shapes:
                    for number in numbers:
                        for filling in fillings:
                            cards.append(Card(color, shape, number, filling))
        self.cards = cards
        #printing info
        print("all cards:")
        print(cards)

    def getSets(self):
        boardcards = self.cards

        sets = []
        for card1 in boardcards:
            for card2 in boardcards:
                if card1 ==  card2:
                    pass
                else:
                    if card1 in boardcards and card2 in boardcards and card1.othercardtoset(card2) in boardcards:
                        theset = [card1, card2, card1.othercardtoset(card2)]
                        theset.sort(key=lambda obj: obj.displaystr)
                        if theset in sets:
                            pass
                        else:
                            sets.append(theset)
        return sets
    


if __name__ == "__main__":
    print(Card.fromstr("ooeg").othercardtoset(Card.fromstr("osp")))



    cards = ["osp", "ooeg", "veg", "~ep", "ooofr","~~sp","vfp","~~~fp","2vsg","2vsp","oofr","ooofp"]
    # for i in range(12):
    #     newcard = False
    #     while not newcard:
    #         newcard = Card.fromstr(input("Card: "))
    #     cards.append(newcard)
    #     print(cards[-1])
    cards = [Card.fromstr(a) for a in cards]
    deck = CardDeck(cards)
    print(deck.getSets())
