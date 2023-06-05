N = int(input())
a = list(map(int, input().split()))

b = sorted(set(a))

answer = {b[i] : i for i in range(len(b))}
for i in a:
    print(answer[i], end=' ')

