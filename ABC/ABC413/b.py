n = int(input())
S = [input() for _ in range(n)]
set = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        set.add(S[i] + S[j])
print(len(set))