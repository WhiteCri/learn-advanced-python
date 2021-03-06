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

print(tag)
from functools import partial
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)