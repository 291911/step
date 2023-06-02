A, B = map(int, input().split())
c = int(input())
n = int(input())

if A * n + B <= c * n and c >= A:
    print(1)
else:
    print(0)