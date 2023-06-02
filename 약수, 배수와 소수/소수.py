N = int(input())
M = int(input())

answer = []
for i in range(N, M+1):
    a = []
    if i > 1:
        for x in range(2, i):
            if i % x == 0:
                a.append(x)
                break
        if len(a) == 0:
            answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))