# base types ignores the Python Design Principle
class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)

dd = DoppelDict(one=1) # __initt__ ignores function overriding
print(dd)
dd['two'] = 2 # overriding worked
print(dd)
dd.update(three=3) #update() ignores function overriding.
# used to modify multiple values at once
print(dd)