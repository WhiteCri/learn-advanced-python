class Gizmo:
    def __init__(self):
        print('Gizmo id : %d' % id(self))

x = Gizmo()
try:
    y = Gizmo() * 10 # 곱셈이 실행되기 전 객체가 먼저 생성됨. 그러나 y는 생성되지 않음
except:
    pass
print(dir())