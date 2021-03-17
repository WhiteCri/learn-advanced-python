from unicodedata import normalize
def nfc_equal(s1, s2):
    return normalize('NFC', s1) == normalize('NFC', s2)

def fold_equal(s1, s2):
    return (normalize('NFC', s1).casefold() == normalize('NFC', s2).casefold())

s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)
print(nfc_equal(s1, s2))

s3 = 'Straße'
s4 = 'Strasse'
print(s3 == s4)
print(nfc_equal(s3, s4))
print(fold_equal(s3, s4))
print(fold_equal(s1, s2))
print(fold_equal('A', 'a'))