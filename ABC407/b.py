X, Y = map(int, input().split())

s = set()
for i in range(1,7):
    for j in range(1,7):
        if i+j >= X:
            s.add((i,j))
        if abs(i-j) >= Y:
            s.add((i,j))

print(len(s)/36)
