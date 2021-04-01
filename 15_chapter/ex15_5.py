import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write # __enter__
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write #__exit

with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
    raise TypeError
print(what)