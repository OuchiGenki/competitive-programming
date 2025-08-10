from itertools import permutations
G = [
    set(map(lambda x: ord(x)-ord('a'), ['b', 'c', 'e', 'h'])),
    set(map(lambda x: ord(x)-ord('a'), ['a', 'c', 'd'])),
    set(map(lambda x: ord(x)-ord('a'), ['a', 'b', 'd', 'g'])),
    set(map(lambda x: ord(x)-ord('a'), ['b', 'c', 'h'])),
    set(map(lambda x: ord(x)-ord('a'), ['a', 'f', 'g', 'i'])),
    set(map(lambda x: ord(x)-ord('a'), ['e', 'h'])),
    set(map(lambda x: ord(x)-ord('a'), ['c', 'e', 'i', 'k'])),
    set(map(lambda x: ord(x)-ord('a'), ['a', 'b', 'd', 'f', 'i', 'k'])),
    set(map(lambda x: ord(x)-ord('a'), ['e', 'g', 'h', 'j'])),
    set(map(lambda x: ord(x)-ord('a'), ['i', 'k'])),
    set(map(lambda x: ord(x)-ord('a'), ['g', 'h', 'j']))
]
n = len(G)
dig = [len(G[i]) for i in range(n)]
ans = set()
for P in permutations(range(n)):
    P = list(P)
    if P[0] != 0:
        continue

    cnt = [0 for _ in range(n)]
    P.append(P[0])
    for i in range(n):
        v, nv = P[i], P[i+1]
        if nv in G[v]:
            cnt[v] += 1
            cnt[nv] += 1
        else:
            break

    flag = True
    for i in range(n):
        if cnt[i] != 2:
            flag = False
            break
    
    if flag:
        print([chr(x + ord('a')) for x in P])
        P = [chr(x + ord('a')) for x in P]
        ans.add(tuple(min(P, list(reversed(P)))))

for i in ans:
    print(i)
