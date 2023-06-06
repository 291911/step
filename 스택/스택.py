import sys

N = int(input())

a = []
for _ in range(N):
    state = sys.stdin.readline().split()
    
    if state[0] == 'push':
        a.append(state[1])
    
    elif state[0] == 'pop':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    
    elif state[0] == 'size':
        print(len(a))
    
    elif state[0] == 'empty':
        if len(a) == 0:
            print(1)
        else:
            print(0)
    
    elif state[0] == 'top':
        if len(a) > 0:
            print(a[-1])
        else:
            print(-1)

