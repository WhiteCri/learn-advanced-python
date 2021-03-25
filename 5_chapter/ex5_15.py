def clip(text, max_len=80):
    '''max_len 앞이나 뒤에 마지막 공백에서 잘라낸 텍스트를 반환한다.
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None: # 공백이 없다
        end = len(text)

    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

print('---------inspect module ----------')
from inspect import signature
sig = signature(clip)
print(sig)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

# kind has five values:
# POSITIONAL_OR_KEYWORD : 위치 인수나 키워드 인수로 전달할 수 있는 매개변수(파이썬 함수 매개벼눗 대부분이 여기에 속한다)
# VAR_POSITIONAL : 위치 매개변수의 튜플
# VAR_KEYWORD: 키워드 매개변수의 딕셔너리
# KEYWORD_ONLY : 키워드 전용 매개변수
# POSITIONAL_ONLY : 위치 전용 배개변수, 현재 파이썬 함수 선언 구문에서는 지원되지 않지만, 키워드로 전달한 매개변수를 받지 않는 DIVMOD()처럼 C언어로 구현된 기존 함수가 여기에 속한다.