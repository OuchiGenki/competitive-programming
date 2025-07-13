T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A = list(map(lambda x: x-1, A))
    
    pos = [[] for _ in range(2*N)]
    for i in range(2*N):
        pos[A[i]].append(i)
    
    ans = set()
    for i in range(2*N-1):
        a, b = A[i], A[i+1]
        a0_pos, a1_pos = pos[a]
        b0_pos, b1_pos = pos[b]
        
        if a0_pos+1 == a1_pos or b0_pos+1 == b1_pos:
            continue
        
        sorted_pos = sorted([a0_pos, a1_pos, b0_pos, b1_pos])
        
        if sorted_pos[0]+1 == sorted_pos[1] and sorted_pos[2]+1 == sorted_pos[3]:
            if a > b:
                a, b = b, a
            ans.add((a, b))

    print(len(ans))
            