N = int(input())

i = 1
a = []
while True:
    i += 1
    if N % i == 0:
        a.append(i)
        N = N // i
        i = 1

    if N == 1:
        break

for i in a:
    print(i)