N = int(input())
size = 50
A = [int('1'*(i+1)) for i in range(size)]
s = set()
for i in range(size):
    for j in range(size):
        for k in range(size):
            s.add(A[i]+A[j]+A[k])
s = sorted(list(s))
print(s[N-1])