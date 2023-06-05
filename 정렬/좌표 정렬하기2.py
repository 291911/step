import sys

N = int(input())
a = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a.append((y, x))

a.sort()

for y, x in a:
    print(x, y)