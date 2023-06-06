N = int(input())
a = []
for _ in range(N):
    A, B = map(str, input().split())
    if A == 'ChongChong' or B == 'ChongChong':
        a.append(A)
        a.append(B)
    if A in a:
        a.append(B)
    if B in a:
        a.append(A)

print(len(set(a)))