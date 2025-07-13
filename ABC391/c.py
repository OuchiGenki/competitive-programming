N, Q = map(int, input().split())
answer = 0
nest = dict()
cnt = dict()
for i in range(1, N+1):
    nest[i] = i
    cnt[i] = 1


for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1], query[2]
        cnt[nest[P]] -= 1
        cnt[H] += 1
        if cnt[nest[P]] == 1:
            answer -= 1
        if cnt[H] == 2:
            answer += 1
        nest[P] = H
    else:
        print(answer)