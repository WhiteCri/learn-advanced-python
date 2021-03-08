import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 14
    suits = 'spades diamonds clubs hearts'.split() # 4

    def __init__(self):
        ## if a member of class has name starts with _, it's protected member
        ## if a member of class has name starts with __, it's private member
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]


    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0], deck[-1])

from random import choice
for i in range(5):
    print(choice(deck))

print(deck[:3])
print(deck[12::13])

print('---')
for card in deck:
    print(card)
print('---')

print('---')
for card in reversed(deck):
    print(card)
print('---')

print(Card('Q', 'hearts') in deck)
print(Card('7', 'hey') in deck)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)