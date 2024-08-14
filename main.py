from set import Card, CardDeck


if __name__ == "__main__":
    fulldeck = CardDeck()

    cards = []
    for i in range(12):
        newcard = False
        while not newcard:
            newcard = Card.fromstr(input("Card: "))
        cards.append(newcard)
        print(cards[-1])


    cards = [Card.fromstr(a) for a in cards]
    deck = CardDeck(cards)
    print(deck.getSets())