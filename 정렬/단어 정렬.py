N = int(input())
a = []

for _ in range(N):
    word = input()
    length = len(word)
    if [length, word] not in a:
        a.append([length, word])

a.sort()

for i in a:
    print(i[1])

