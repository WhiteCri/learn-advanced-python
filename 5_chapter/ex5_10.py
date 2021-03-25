def tag(name, *content, cls=None, **attrs):
    '''하나 이상의 HTML 태그를 생성한다'''
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello', 'world')) # hello, world는 튜플로 들어감
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag)) # dict안의 항목은 별도의 인수로 전달되며, 나머지는 attrs에 전달

def f(a, *, b):
    return a, b

print(f(1, b=2))