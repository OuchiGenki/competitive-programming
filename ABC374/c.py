N = int(input())
K = list(map(int, input().split()))
answer = float('inf')
for i in range(2**N):
    cnt_A = 0
    cnt_B = 0
    for j in range(N):
        if (i>>j) & 1:
            cnt_A += K[j]
        else:
            cnt_B += K[j]
    answer = min(answer, max(cnt_A, cnt_B))
print(answer)