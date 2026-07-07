class Deck:

    def __init__(self):
        self.cards = [
            "Ace of Hearts",
            "King of Hearts",
            "Queen of Hearts",
            "Jack of Hearts"
        ]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.cards):

            card = self.cards[self.index]
            self.index += 1
            return card

        raise StopIteration

    def __repr__(self):
        return f"Deck({len(self.cards)} cards)"


deck = Deck()

print(deck)

print("\nDealing Cards:")

for card in deck:
    print(card)