n = int(input())

flag = True
c1 = {'H', 'D', 'C', 'S'}
c2 = {'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'}
seen = set()
for i in range(n):
    s = input()
    if s in seen:
        flag = False
    if s[0] not in c1 or s[1] not in c2:
        flag = False
    seen.add(s)

if flag:
    print("Yes")
else:
    print("No")