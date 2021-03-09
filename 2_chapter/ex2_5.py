symbols = '$*@(#$asdf✔'
t = tuple(ord(symbol) for symbol in symbols)
print(t)

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

