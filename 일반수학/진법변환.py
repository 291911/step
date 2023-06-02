B, N = map(str, input().split())

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = 0

for i in range(len(B)):
    if B[i] in alphabet:
        a = alphabet.index(B[i]) + 10
        b = int(N) ** (len(B) - i - 1)
        answer += a * b
    else:
        a = int(B[i])
        b = int(N) ** (len(B) - i - 1)
        answer += a * b

print(answer)



