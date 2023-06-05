import sys

N = int(input())
a = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a.append((x, y))

a.sort()

for i in range(N):
    print(a[i][0], a[i][1])