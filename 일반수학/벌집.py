N = int(input())

answer = 0
i = 0
b = 1
while True:
    a = 6 * i
    b += a
    answer += 1
    i += 1
    if b >= N:
        break

print(answer)

