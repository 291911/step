import sys

N = int(sys.stdin.readline())
a = [0] * 10001

for _ in range(N):
    a[int(sys.stdin.readline())] += 1

for i in range(10001):
    if a[i] != 0:
        for j in range(a[i]):
            print(i)