from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = []


combi = list(combinations(cards, 3))
for i in combi:
    if sum(i) <= M:
        answer.append(sum(i))

print(max(answer))

