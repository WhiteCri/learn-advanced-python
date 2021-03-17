city = 'São Paulo' # code point. just a string
city = 'Montréal'
r = city.encode('utf_8') #real byte array representation
print(r)
r = city.encode('utf_16')
print(r, type(r))
r = city.encode('iso8859_1')
print(r)
#r = city.encode('cp437')
r = city.encode('cp437', errors='ignore')
print(r)
r = city.encode('cp437', errors='replace')
print(r)
r = city.encode('cp437', errors='xmlcharrefreplace')
print(r)


