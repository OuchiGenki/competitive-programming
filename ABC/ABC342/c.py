N = int(input())
S = input()
Q = int(input())
C, D = [], []
for i in range(Q):
    c, d = input().split()
    C.append(c)
    D.append(d)

dist = [''] * 26
for i in range(N):
    dist[ord(S[i]) - ord('a')] = S[i]

for i in range(26):
    for j in range(Q):
        c, d = C[j], D[j]
        if c != dist[i]:
            continue
        dist[i] = d

ans = ''
for i in range(N):
    ans += dist[ord(S[i]) - ord('a')]

print(ans)