from itertools import permutations
s = input()
atc = 'atcoder'
n = len(s)
ans = float('inf')
for p in permutations(range(n)):
    flag = True
    for i in range(n):
        if atc[i] != s[p[i]]:
            flag = False
        
    if flag:
        cnt = 0
        for i in range(n):
            for j in range(i):
                if p[j] > p[i]:
                    cnt += 1
        ans = min(ans, cnt)
print(ans)