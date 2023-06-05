N, M = map(int, input().split())

names = set()
for _ in range(N):
    a = input()
    names.add(a)

answer = set()
for _ in range(M):
    b = input()
    answer.add(b)

result = sorted(list(names & answer))
print(len(result))
for i in result:
    print(i)