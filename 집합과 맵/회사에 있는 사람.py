N = int(input())
a = {}
for _ in range(N):
    name, state = map(str, input().split())
    if name not in a and state == 'enter':
        a[name] = 1
    elif name not in a and state == 'leave':
        a[name] = 0
    elif name in a and state == 'enter':
        a[name] = 1
    elif name in a and state == 'leave':
        a[name] = 0

answer = sorted(a, reverse=True)
for i in answer:
    if a[i] == 1:
        print(i)

