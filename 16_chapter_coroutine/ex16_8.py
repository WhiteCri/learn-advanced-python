class DemoException(Exception):
    '''설명에 사용할 예외 유형'''

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run!')

exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
exc_coro.close()
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))

print('ex16_10')
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))
print(exc_coro.send(20215182))

print('ex16_11')
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
exc_coro.throw(ZeroDivisionError)
print(getgeneratorstate(exc_coro))