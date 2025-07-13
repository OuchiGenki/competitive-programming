N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

answer = 0
b_idx = 0
w_idx = 0

while b_idx < N and B[b_idx] >= 0:
    answer += B[b_idx]
    b_idx += 1
while w_idx < M and W[w_idx] >= 0 and w_idx < b_idx:
    answer += W[w_idx]
    w_idx += 1
    
if b_idx > w_idx:
    print(answer)
    exit()

while b_idx < N and w_idx < M and B[b_idx] + W[w_idx] >= 0:
    answer += B[b_idx] + W[w_idx]
    b_idx += 1
    w_idx += 1
    
print(answer)