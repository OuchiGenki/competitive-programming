n = int(input())
s = [input() for i in range(n)]
s.reverse()
for i in range(n):
    print(s[i])