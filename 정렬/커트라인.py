N, k = map(int, input().split())
a = list(map(int, input().split()))

a_srt = sorted(a, reverse=True)
print(a_srt[k-1])
