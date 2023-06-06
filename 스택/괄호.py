N = int(input())

for _ in range(N):
    s = input()

    a = 0
    for i in s:
        if i == '(':
            a += 1
        else:
            a -= 1

        if a < 0:
            print('NO')
            break
    if a > 0:
        print('NO')
    elif a == 0:
        print('YES')