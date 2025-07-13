n = int(input())
s = [input() for i in range(n)]
name = set()
for i in range(n):
    if s[i] not in name:
        name.add(s[i])
        print(i+1)