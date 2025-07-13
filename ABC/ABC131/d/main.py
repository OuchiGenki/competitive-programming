n = int(input())
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a,b))
ab.sort(key = lambda x: x[1])

time = 0
flag = True
for i in range(n):
    time += ab[i][0]
    if time > ab[i][1]:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")