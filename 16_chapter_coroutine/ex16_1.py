def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ')

my_coro = simple_coroutine()
print(my_coro)

print('print : ' , next(my_coro))
#my_coro.send(42)

## coroutine has 4 states...
# GEN_CREATED
# GEN_RUNNING
# GEN_SUSPENDED
# GEN_CLOSED

my_coro = simple_coroutine()
my_coro.send(1729)