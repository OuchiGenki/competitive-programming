import sys
from itertools import permutations
sys.setrecursionlimit(10**8)

n = int(input())
r = input()
c = input()

la = [i for i in range(n)]
lb = [i for i in range(n)]
lc = [i for i in range(n)]

ans = [['.' for i in range(n)] for j in range(n)]
idx = 0
for A in permutations(la):
    for B in permutations(la):
        for C in permutations(la):
            flag = 0
            for i in range(n):
                if A[i]==B[i] or B[i]==C[i] or C[i]==A[i]:
                    flag = 1

            rs = ""
            for i in range(n):
                for j in range(n):
                    if A[i] == j:
                        rs += 'A'
                        break
                    if B[i] == j:
                        rs += 'B'
                        break
                    if C[i] == j:
                        rs += 'C'
                        break
            if rs != r:
                flag = 1

            cs = ""
            for i in range(n):
                for j in range(n):
                    if A[j] == i:
                        cs += 'A'
                        break
                    if B[j] == i:
                        cs += 'B'
                        break
                    if C[j] == i:
                        cs += 'C'
                        break
            if cs != c:
                flag = 1

            if flag:
                continue

            for i in range(n):
                ans[i][A[i]] = 'A'
                ans[i][B[i]] = 'B'
                ans[i][C[i]] = 'C'

            print("Yes")
            for a in ans:
                print("".join(a))
            exit()

print("No")