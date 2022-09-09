import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))

    print(f'The first card {deck[0]}')
    print(f'The last card {deck[-1]}')
    print()

    print(f'The first random card {choice(deck)}')
    print(f'The second random card {choice(deck)}')
    print(f'The third random card {choice(deck)}')

if __name__ == '__main__':
    main()

