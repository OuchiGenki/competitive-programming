n = int(input())
s = list(input())

cnt = []
tmp = 0
for i in range(n):
    if s[i] == '(':
        tmp += 1
    else:
        tmp -= 1
    cnt.append(tmp)
s = ['(' for i in range(-min(cnt))] + s

cnt = []
tmp = 0
for i in range(len(s)):
    if s[i] == '(':
        tmp += 1
    else:
        tmp -= 1
    cnt.append(tmp)
s = s + [')' for i in range(cnt[-1])]

print(*s, sep="")