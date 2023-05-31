A, B, V = map(int, input().split())

answer = 0

answer += (V - A) // (A - B) + 1
if (V - A) % (A - B) != 0:
    answer += 1

    
print(answer)