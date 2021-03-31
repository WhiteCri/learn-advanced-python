import collections

Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


from random import shuffle
l = list(range(10))
shuffle(l)
print(l)

deck = FrenchDeck()
#shuffle(deck)

def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card # modifying class method in runtime
shuffle(deck)
print(deck._cards)

print('duck typing')
field_names = 'askjdf;lsa sjdfksd, asdfsdf'
try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError:
    pass
field_names = tuple(field_names)