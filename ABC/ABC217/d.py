from sortedcontainers import SortedSet

l, q = map(int, input().split())
S = SortedSet()
S.add(0)
S.add(l)
for i in range(q):
    c, x = map(int, input().split())
    if c == 1:
        S.add(x)
    elif c == 2:
        left_idx = S.bisect(x)-1
        right_idx = S.bisect(x)
        print(S[right_idx] - S[left_idx])