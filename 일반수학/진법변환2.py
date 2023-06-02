N, B = map(int, input().split())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''

while True:
    a = N // B
    b = N % B
    if b >= 10:
        answer += alphabet[b-10]
        N = a

    if b < 10:
        answer += str(b)
        N = a

    if a == 0:
        break

print(answer[::-1])
