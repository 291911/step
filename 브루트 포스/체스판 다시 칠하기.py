N, M = map(int, input().split())
board = []
answer = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        first_w = 0
        first_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] !='W':
                        first_w += 1
                    else:
                        first_b += 1
                else:
                    if board[x][y] != 'W':
                        first_b += 1
                    else:
                        first_w += 1
        
        answer.append(first_w)
        answer.append(first_b)

print(min(answer))