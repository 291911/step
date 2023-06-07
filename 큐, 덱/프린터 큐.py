from collections import deque

N = int(input())

for _ in range(N):
    l, a = map(int, input().split())
    q = deque([map(int, input().split())])
    idx = deque([x for x in range(l)])
    answer = 0
 
    while q:
        if q[0] == max(q):
            answer += 1
            q.popleft()
            idx_pop = idx.popleft()
            if idx_pop == a:
                print(answer)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())

# 다시해보기