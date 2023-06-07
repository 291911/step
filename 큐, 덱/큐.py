import sys
from collections import deque
N = int(input())

q = deque([])
for _ in range(N):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        q.append(a[1])

    elif a[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
            
    elif a[0] == 'size':
        print(len(q))
    
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif a[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])


# deque를 import 하는 방법도 있지만
# 변수를 선언해서 pop하지 말고 그냥 print(a[i])를 해서
# 인덱스 변화를 없애는 방법도 있음

