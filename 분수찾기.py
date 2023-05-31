N = int(input())

i = 1
a = 0

while True:
    a += i
    if a >= N:
        a -= i
        break
    i += 1

n = N - a
up = n
down = i + 1 - n

if i % 2 == 0:
    print(str(up)+"/"+str(down))
else:
    print(str(down)+"/"+str(up))
