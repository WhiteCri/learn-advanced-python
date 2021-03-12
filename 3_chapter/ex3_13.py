from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
# chr(integer) : return unicode of the integer
# opposite to ord()

## dictionary analysis
# 1. An element must be hashable
# 2. Memory efficienty is quite bad, since it has to maintain hash table
# 3. key searching is super fast, since it's based on hashing
# 4. If there's duplication of key, the order is same with insertion order
DIAL_CODES = [
(86, 'China'),
(91, 'India'),
(1, 'United States'),
(62, 'Indonesia'),
(55, 'Brazil'),
(92, 'Pakistan'),
(880, 'Bangladesh'),
(234, 'Nigeria'),
(7, 'Russia'),
(81, 'Japan'),
]

d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3

# 5. if there's insertion, key ordering might be changed