import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence): # absract method is evaluated in runtime
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, pos, value):
        self._cards[pos] = value

    def __delitem__(self, position): # abstract method
        del self._cards[position]

    def insert(self,position, value): # abstract method
        self._cards.insert(position, value)