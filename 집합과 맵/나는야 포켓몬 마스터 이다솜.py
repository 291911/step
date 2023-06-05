import sys
N, M = map(int, input().split())

dogam = {}
i = 1
for _ in range(N):
    name = str(sys.stdin.readline()).strip()
    if name not in dogam:
        dogam[name] = i
    i += 1

dogam_list = list(dogam)
for _ in range(M):
    Q = str(sys.stdin.readline()).strip()
    if Q in dogam:
        print(dogam[Q])
    else:
        print(dogam_list[int(Q)-1])
