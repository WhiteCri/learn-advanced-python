class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('span'))

brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USB'.format(rate=brl))
print(format(42, 'b'))
print(format(2/3, '.1%'))

from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))