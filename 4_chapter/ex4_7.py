octets = b'Montr\xe9al' #Montréal
r = octets.decode('cp1252')
print(r)
r = octets.decode('iso8859_7') #Greek language. Strange conversion
print(r)
r = octets.decode('koi8_r') # russian
print(r)
# r = octets.decode('utf_8') # can not decode with utf-8
r = octets.decode('utf_8', errors='replace') #
print(r)