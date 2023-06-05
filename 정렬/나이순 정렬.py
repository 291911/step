import sys

N = int(input())
a = []

i = 1
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    a.append((int(age), name, i))
    i += 1

a.sort(key = lambda x : (x[0], [2]))

for j in a:
    print(j[0], j[1])