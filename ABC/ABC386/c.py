K = input()
S = input()
T = input()

if len(S) == len(T):
    diff = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            diff += 1
    if diff <= 1:
        print("Yes")
    else:
        print("No")

elif len(S) - len(T) == 1:
    s_idx = 0
    t_idx = 0
    diff = 0
    while s_idx < len(S):
        if S[min(s_idx, len(S)-1)] != T[min(t_idx, len(T)-1)]:
            diff += 1
            s_idx += 1
        else:
            s_idx = min(len(S), s_idx+1)
            t_idx = min(len(T), t_idx+1)
    if diff <= 1:
        print("Yes")
    else:
        print("No")

elif len(T) - len(S) == 1:
    s_idx = 0
    t_idx = 0
    diff = 0
    while t_idx < len(T):
        if S[min(s_idx, len(S)-1)] != T[min(t_idx, len(T)-1)]:
            diff += 1
            t_idx += 1
        else:
            s_idx += 1
            t_idx += 1
    if diff <= 1:
        print("Yes")
    else:
        print("No")

else:
    print("No")