import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 13 + 123 = 93 + 103.") # copying from pdf does not work..

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))
print('  bytes:', re_numbers_bytes.findall(text_bytes)) # can not process about digits that exceed the range of ascii
print('Words')
print('  str  :', re_words_str.findall(text_str))
print('  bytes:', re_words_bytes.findall(text_bytes))