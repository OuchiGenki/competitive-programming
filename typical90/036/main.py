n, q = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(n)]
xy = [[i-j, i+j] for i, j in xy]
SortByX = sorted(xy, key=lambda x: x[0])
SortByY = sorted(xy, key=lambda x: x[1])

for i in range(q):
    a = int(input())
    print(max(abs(SortByX[0][0]-xy[a-1][0]), abs(SortByX[len(xy)-1][0]-xy[a-1][0]), abs(SortByY[0][1]-xy[a-1][1]), abs(SortByY[len(xy)-1][1]-xy[a-1][1])))