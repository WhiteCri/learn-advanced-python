# coding: utf_8
print('Olá, Mundo!')

# $ chardetect 04-text-byte.asciidoc

u16 = 'El Niño'.encode('utf_16')
# b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00
# \xff\xfe is BOM(Byte Order Mark)
print(u16)

u16le = 'El Niño'.encode('utf_16le')
print(list(u16le))
u16be = 'El Niño'.encode('utf_16be')
print(list(u16be))