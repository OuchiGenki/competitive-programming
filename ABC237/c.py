import numpy as np
H, W = map(int, input().split())
A = np.array([list(map(int, input().split())) for i in range(H)])
A = A.T
for i in A:
    print(*i)