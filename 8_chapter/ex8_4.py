alex = {'name': 'Charles L. Dodgson', 'born':1832, 'balance':950}
charles = {'name': 'Charles L. Dodgson', 'born':1832, 'balance':950}
print(alex == charles) # == : compare the contents. calls __eq__ internally
print(alex is charles) # is : compare the id

x = 1
print(x is None) # 'is' can not be overloaded
print(x is not None)
