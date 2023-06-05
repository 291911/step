N, M = map(int, input().split())
answer = 0
s = []
for _ in range(N):
    s.append(input())

for _ in range(M):
    if input() in s:
        answer += 1
    
print(answer)