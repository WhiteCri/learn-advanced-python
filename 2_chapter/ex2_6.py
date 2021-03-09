lax_coordinates = (33.9425, -119.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA204856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

latitude, longitude = lax_coordinates
print(latitude, longitude)
# a, b = b, a
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

import os
_, filename = os.path.split('/home/tw-asl/catkin_ws/devel/setup.sh')
print(filename)

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, b, rest = range(3)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

