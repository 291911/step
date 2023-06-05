N = int(input())
a = []
for _ in range(N):
    a.append(int(input()))

a = sorted(a)
for i in a:
    print(i)