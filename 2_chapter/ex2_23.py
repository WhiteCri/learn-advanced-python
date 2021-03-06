from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)

print(dq.rotate(3))
print(dq)

print(dq.rotate(-4))
print(dq)

print(dq.appendleft(-1))
print(dq)

print(dq.extend([11, 22, 33]))
print(dq)

print(dq.extendleft([10, 20, 30, 40]))
print(dq)