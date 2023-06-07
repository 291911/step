from collections import deque
import sys

T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    rev, flag = 0, 0
    
    for i in p:
        if i == 'R':
            rev += 1

        elif i == 'D':
            if len(arr) > 0:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                flag += 1
                break

    if flag == 0:
        if rev % 2 == 0:
            print('['+','.join(map(str, arr))+']')
        else:
            arr.reverse()
            print('['+','.join(map(str, arr))+']')
