N = int(input())
a = []
answer = 0
for _ in range(N):
    state = str(input())
    if state != 'ENTER':
        a.append(state)
    else:
        answer += len(set(a))
        a = []

answer += len(set(a))
print(answer)