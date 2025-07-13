N, K = map(int, input().split())
S = [int(input()) for i in range(N)]

if 0 in S:
    print(N)
    exit()

right = 0
product = 1
ans = 0
for left in range(N):
    while right < N and product * S[right] <= K:
        product *= S[right]
        right += 1
    ans = max(ans, right-left)
    if right == left:
        right += 1
    else:
        product //= S[left]

print(ans)