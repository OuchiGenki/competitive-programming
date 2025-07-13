from collections import defaultdict

S = input()
d = defaultdict(int)
for c in S:
    d[c] += 1

for i in range(26):
    c = chr(ord('a') + i)
    if d[c] == 0:
        print(c)
        exit()