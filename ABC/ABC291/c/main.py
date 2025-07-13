n = int(input())
s = input()
x = y = 0
pos = set()
pos.add((x, y))
for i in s:
    if i=='R':
        x += 1
    if i=='L':
        x -= 1
    if i=='U':
        y += 1
    if i=='D':
        y -= 1
    pos.add((x, y))

if len(pos) == n+1:
    print("No")
else:
    print("Yes")