import queue

Q = queue.Queue(maxsize=20)

for v in range(1, 10):
    Q.put(v)
print("큐의 내용: ", end='')
for _ in range(1, 10):
    print(Q.get(), end=' ')
print()

S = queue.LifoQueue(maxsize=20)

for v in range(1, 10):
    S.put(v)
print("스택의 내용: ", end='')
for _ in range(1, 10):
    print(S.get(), end=' ')
print()