N = int(input())
a = []
for i in range(1, N+1):
    num = sum(map(int, str(i)))
    if i + num == N:
        a.append(i)
        print(i)
        break

if len(a) == 0:
    print(0)
