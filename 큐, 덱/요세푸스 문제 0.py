from collections import deque
N, K = map(int, input().split())

a = deque([i for i in range(1, N+1)])
answer = []

while a:
    for i in range(K-1):
        a.append(a.popleft())
    answer.append(a.popleft())

print('<' + ', '.join(map(str, answer)) + '>', end='')
