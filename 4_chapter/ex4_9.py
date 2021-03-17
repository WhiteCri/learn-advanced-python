# open('cafe.txt', 'w', encoding='utf_16').write('café')
# if we skip encoding, it uses local codings in computer
# print(open('cafe.txt').read())

fp = open('cafe.txt', 'w', encoding='utf_16')
print(fp)
fp.write('café')
fp.close()

import os
print(os.stat('cafe.txt').st_size) # file length(byte)

fp2 = open('cafe.txt')
print(fp2.encoding)
# print(fp2.read()) # error : encoding/decoding does not match

fp3 = open('cafe.txt', encoding='utf-16')
print(fp3)
print(fp3.read())

fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())