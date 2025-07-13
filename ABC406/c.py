N = int(input())
A = list(map(int, input().split()))

L = [0]
for i in range(1, N-1):
    if A[i-1] < A[i] and A[i] > A[i+1]:
        L.append(i)
    if A[i-1] > A[i] and A[i] < A[i+1]:
        L.append(i)
L.append(N-1)

if A[0] < A[1]:
    case = 1
else:
    case = 2

answer = 0
if case == 1:
    for i in range(1, len(L), 2):
        if i+2 >= len(L):
            continue
        answer += (L[i]-L[i-1]) * (L[i+2]-L[i+1])
if case == 2:
    for i in range(2, len(L), 2):
        if i+2 >= len(L):
            continue
        answer += (L[i]-L[i-1]) * (L[i+2]-L[i+1])   

print(answer)
