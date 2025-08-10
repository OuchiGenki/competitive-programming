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
dp = [[float('inf')] * n for _ in range(1 << n)]
dp[0][0] = 0
for S in range(2**n):
    