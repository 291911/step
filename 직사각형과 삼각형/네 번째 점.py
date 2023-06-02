a = []
b = []
for i in range(3):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

a = sorted(a)
b = sorted(b)

if a.count(a[0]) == 1:
    w = a[0]
else:
    w = a[-1]

if b.count(b[0]) == 1:
    h = b[0]
else:
    h = b[-1]

print(w, h)
