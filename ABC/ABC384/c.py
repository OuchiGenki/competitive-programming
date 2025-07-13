points = list(map(int, input().split()))

scores = []
for i in range(1, 2**5):
    score = 0
    name = ''
    for j in range(5):
        if i >> j & 1:
            score += points[j]
            name += chr(ord('A')+j)
    scores.append((score, name))

#一旦照準ソートするとよいかも？
scores.sort(key=lambda x: (-x[0], x[1]))

for i in scores:
    print(i[1])
    