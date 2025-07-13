n = int(input())
s = input()

cnt_o = 0
cnt_x = 0
res = 0

for i in range(n):
    if s[i] == "o":
        cnt_o += 1
        res += cnt_x*(cnt_x-1)//2
        cnt_x = 0
    else:
        cnt_x += 1
        res += cnt_o*(cnt_o-1)//2
        cnt_o = 0

res += cnt_o*(cnt_o-1)//2
res += cnt_x*(cnt_x-1)//2

print(n*(n-1)//2-res)
