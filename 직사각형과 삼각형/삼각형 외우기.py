triangle = []

for _ in range(3):
    triangle.append(int(input()))

if sum(triangle) == 180 and len(set(triangle)) == 1:
    print('Equilateral')
elif sum(triangle) == 180 and len(set(triangle)) == 2:
    print('Isosceles')
elif sum(triangle) == 180 and len(set(triangle)) == 3:
    print('Scalene')
elif sum(triangle) != 180:
    print('Error')