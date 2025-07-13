N = int(input())
S = input()
ans = 0

for i in range(26):
    c = chr(ord('a') + i)
    right = 0
    res = 0
    for left in range(N):
        while right < N and S[right] == c:
            right += 1
        res = max(res, right - left)
        if left == right:
            right += 1
    ans += res

print(ans)