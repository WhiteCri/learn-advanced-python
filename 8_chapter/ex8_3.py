charles = {'name': 'Charles L. Dodgson', 'born':1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)