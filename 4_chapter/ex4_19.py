# sorting unicode text
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

import locale
print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')) #not working in my computer
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)