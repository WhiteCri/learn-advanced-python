class AnswerDict(dict):
    def __getitem__(self, item):
        return 42

ad = AnswerDict(a='foo')
print(ad['d'])

d = {}
d.update(ad)
print(d['a'])
print(d)