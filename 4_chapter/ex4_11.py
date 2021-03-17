import sys, locale

# this program will executed differently pc by pc
expressions = '''
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.stderr.isatty()
sys.stderr.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
'''
my_file = open('dummy', 'w')

for expr in expressions.split():
    value = eval(expr)
    print(expr.rjust(30), '->', repr(value))

# sys.getdefaultencoding() is used to  encode file name

s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)
# above s1, s2 must be handled same in Standard Unicode, but python doesn't

from unicodedata import normalize
s1 = 'café'
s2 = 'cafe\u0301'
print(len(s1), len(s2))

print(len(normalize('NFC', s1)), len(normalize('NFC', s2))) # transform to shortest
print(len(normalize('NFD', s1)), len(normalize('NFD', s2))) # decomposite combined character
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

#sometimes, normalize generates different character

from unicodedata import name
ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))

print(ohm == ohm_c)
print(normalize('NFC', ohm), normalize('NFC', ohm_c))
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))


fi = 'ﬁ'
print(normalize('NFKC', fi))
four_squared = '42'
print(normalize('NFKC', four_squared))

micro = 'μ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))
# NFKC, NFKD may results in damage on original data

print('----------- case folding-------------')
micro = 'μ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)

eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)