S = input()
N = len(S)
Q = int(input())
K = list(map(int, input().split()))
ans = []
for k in K:
    k -= 1
    x = k // N
    if x.bit_count() % 2 == 0:
        ans.append(S[k%N])
    else:
        ans.append(S[k%N].swapcase())
print(*ans)