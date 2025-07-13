N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = []
for i in range(N):
    AB.append((A[i], B[i]))

AB.sort(reverse=True, key=lambda x: x[0])

sum1 = 0
cnt1 = 0
for i in range(N):
    sum1 += AB[i][0]
    cnt1 += 1
    if sum1 > X:
        break

AB.sort(reverse=True, key=lambda x: x[1])

sum2 = 0
cnt2 = 0
for i in range(N):
    sum2 += AB[i][1]
    cnt2 += 1
    if sum2 > Y:
        break

print(min(cnt1, cnt2))
