from collections import defaultdict

S = input()
lcnt = defaultdict(int)
rcnt = defaultdict(int)

for c in S:
    rcnt[c] += 1

ans = 0
for c in S:
    rcnt[c] -= 1
    for i in range(26):
        ans += lcnt[chr(ord('A')+i)] * rcnt[chr(ord('A')+i)]
    lcnt[c] += 1

print(ans)
