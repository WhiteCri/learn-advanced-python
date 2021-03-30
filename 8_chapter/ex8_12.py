# do not use variance parameter as an default parameter!
class HauntedBus:
    '''유령 승객이 출몰하는 버스 모델'''
    def __init__(self, passengers = []):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name) # this actually changes default parameter

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)
print(id(bus1.passengers), id(bus3.passengers))

print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)