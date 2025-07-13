N = int(input())
U = set()
ans = 0
for i in range(N):
    S = input()
    if S not in U:
        ans += 1
        U.add(S)
        U.add(S[::-1])
print(ans)