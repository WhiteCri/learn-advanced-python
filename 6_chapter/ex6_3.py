# implementation of strategy pattern in pythonic way
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self) ## 이전과 달라진 점
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

## we don't have to use @abstract method anymore

def fidelity_promo(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() *.1

def large_order_promo(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0