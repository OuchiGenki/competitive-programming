A = [4, 90, 25, 30, 30, 8, 90, 90]
S = sorted(list(set(A)))
ranking = {x:i+1 for i, x in enumerate(S)}
for i in range(len(A)):
    A[i] = ranking[A[i]]
print(A)    # [1, 5, 3, 4, 4, 2 ,5, 5]