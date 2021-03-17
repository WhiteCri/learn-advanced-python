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