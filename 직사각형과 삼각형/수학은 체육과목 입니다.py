N = int(input())

w = []
h = []
for _ in range(N):
    A, B = map(int, input().split())
    w.append(A)
    h.append(B)
    
print((max(w)-min(w)) * (max(h)-min(h)))
