import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

color = [-1 for i in range(n)]

def calc(n):
    return (n*(n-1))//2

def dfs(t):
    global cnt_b
    global cnt_w
    global ngFlag
    
    if color[t] == 0:
        cnt_w += 1
    else:
        cnt_b += 1

    for nt in g[t]:
        #同じ色が並んでいたら二部グラフではない
        if color[t] == color[nt]:
            ngFlag = True

        # 訪問済みならスキップ
        if color[nt] != -1:
            continue

        # 白黒の塗り分け
        if color[t] == 0:
            color[nt] = 1
        else:
            color[nt] = 0
        
        dfs(nt)

res = 0
ngFlag = False  #二部グラフでない時True
for i in range(n):
    # 訪問済みならスキップ
    if color[i] != -1:
        continue

    cnt_w = 0   #白の個数
    cnt_b = 0   #黒の個数
    color[i] = 0 #開始点は白
    dfs(i)
    res += calc(cnt_w) + calc(cnt_b)    #結ばない線を加算

if ngFlag:
    print(0)
else:
    print(calc(n) - m - res)