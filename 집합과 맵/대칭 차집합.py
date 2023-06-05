A, B = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_b = set(a) - set(b)
b_a = set(b) - set(a)
print(len(a_b | b_a))