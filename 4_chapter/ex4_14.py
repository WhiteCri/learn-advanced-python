import unicodedata
import string

def shave_marks(txt):
    '''발음 구별 기호를 모두 제거한다.'''
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)