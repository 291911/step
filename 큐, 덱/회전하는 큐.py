from collections import deque

N, M = map(int, input().split())
wanted = list(map(int, input().split()))

q = deque([i for i in range(1, N+1)])
idx = [i for i in range(1, N+1)]

answer = 0
x = 0
for i in wanted:
    if q[0] == i:
        q.popleft()
    
    else:
        if q.index(i) <= len(q) - q.index(i):
            while True:
                q.append(q.popleft())
                answer += 1

                if q[0] == i:
                    q.popleft()
                    break
                

        elif q.index(i) > len(q) - q.index(i):
            while True:
                q.appendleft(q.pop())
                answer += 1
                
                if q[0] == i:
                    q.popleft()
                    break
 
    

print(answer)

