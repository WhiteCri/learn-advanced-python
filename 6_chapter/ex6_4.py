from ex6_3 import *

joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100) # number means 'fidelity'
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]


print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, bulk_item_promo()))

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))