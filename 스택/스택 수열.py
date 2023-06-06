import sys
N = int(input())
answer = []
stack = []
i = 1
end = 0
for _ in range(N):
    a = int(sys.stdin.readline())

    while i <= a:
        stack.append(i)
        answer.append('+')
        i += 1

    if a == stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        print('NO')
        end += 1
        break

if end == 0:
    for i in answer:
        print(i)