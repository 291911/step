N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))

n_dict = {i : 1 for i in n_nums}

answer = [] 
for j in m_nums:
    if j not in n_dict:
        answer.append(0)
    else:
        answer.append(1)       

for x in answer:
    print(x, end=' ')
