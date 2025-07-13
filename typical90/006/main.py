n, k = map(int, input().split())
s = input()

next = [[n for i in range(26)] for j in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(26):
        if ord(s[i]) == 97 + j:
            next[i][j] = i
        else:
            next[i][j] = next[i+1][j]

ans = []
pos = 0
for i in range(k):
    for j in range(26):
        if next[pos][j] <= n-k+i:
            pos = next[pos][j]+1
            ans.append(chr(97+j))
            break
print(*ans, sep="")