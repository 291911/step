N = int(input())
n_cards = list(map(int, input().split()))
M = int(input())
m_cards = list(map(int, input().split()))

n_dict = {}
for i in n_cards:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

answer = []
for j in m_cards:
    if j in n_dict:
        answer.append(n_dict[j])
    else:
        answer.append(0)
    
for x in answer:
    print(x, end=' ')