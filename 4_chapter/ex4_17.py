import unicodedata
import string

def shave_marks_latin(txt):
    '''라틴 기반 문자에서 발음 구별 기호를 모두 제거한다'''
    norm_txt = unicodedata.normalize('NFD', txt) # decomposite
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

print(len("""‚ƒ„†ˆ‹‘’“”•–̃ ̃"""))
print(len("""'f"*^<''""---~>"""))
single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–— ̃›""", """'f"*^<''""---~>""")


multi_map = str.maketrans({
'€': '<euro>',
'...': '...',
'Œ': 'OE',
'TM': '(TM)',
'œ': 'oe',
'‰': '<per mille>',
'‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)

# ex4_18

order = '“Herr Voß: • 1⁄2 cup of ŒtkerTM caffè latte • bowl of açaí.”'
print(dewinize(order))
print(asciize(order))