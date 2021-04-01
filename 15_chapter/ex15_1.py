from collections import namedtuple
D = namedtuple('D', 'flaver')
my_list = list(D('hello') for i in range(3))
for item in my_list:
    if item.flaver == 'banana':
        break
#else:
#    raise ValueError('No banana flaver found!')

with open('mirror.py') as fp: # open('mirror.py) is just return of instance, fp is result of __enter__()
    src = fp.read(60)
    # exit is called