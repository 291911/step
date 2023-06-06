T = int(input())

for _ in range(T):
    n, k = map(int, input().split())

    a = 1
    for i in range(min(n, k)):
        a *= max(n, k)-i

    b = 1
    for j in range(1, min(n, k)+1):
        b *= j

    print(a // b)