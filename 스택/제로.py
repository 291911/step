import sys

K = int(sys.stdin.readline())
a = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        a.append(num)
    else:
        a.pop()

print(sum(a))
