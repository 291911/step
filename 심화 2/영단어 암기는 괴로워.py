import sys
N, M = map(int, input().split())

words = {}
for _ in range(N):
    a = sys.stdin.readline().strip()
    if len(a) >= M:
        if a in words:
            words[a] += 1
        else:
            words[a] = 1

w_dict = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for j in w_dict:
    print(j[0])
