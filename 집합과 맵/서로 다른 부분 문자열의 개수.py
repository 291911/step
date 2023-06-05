s = str(input())

answer = []

for i in range(len(s)):
    for j in range(i, len(s)+1):
        if s[i:j] != '':
            answer.append(s[i:j])

print(len(set(answer)))