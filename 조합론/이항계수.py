n, k = map(int, input().split())

a = 1
for i in range(k):
    a *= n-i

b = 1
for j in range(1, k+1):
    b *= j

print(a)