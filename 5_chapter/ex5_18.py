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

import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}

bound_args = sig.bind(**my_tag)
print(bound_args)
for name, value in bound_args.arguments.items():
    print(name, '=', value)

del my_tag['name']
bound_args = sig.bind(**my_tag)
