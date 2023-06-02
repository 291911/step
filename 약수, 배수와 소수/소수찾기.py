N = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in nums:
    a = []
    for x in range(1, i):
        if i % x == 0:
            a.append(i)
    if len(a) == 1:
        answer += 1

print(answer)
