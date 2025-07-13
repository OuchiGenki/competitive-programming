def main():
    def isOK(index, sum):
        if sum + s[index] <= m:
            return True
        else:
            return False

    n, m = map(int, input().split())
    p = [0]
    for i in range(n):
        p.append(int(input()))
    p.sort()

    s = set()
    for i in p:
        for j in p:
            if i+j <= m:
                s.add(i+j)
            else:
                break
    s = list(sorted(s))

    ans = 0
    for i in s:
        ok = -1
        ng = len(s)
        while ng-ok>1:
            mid = (ok+ng)//2
            if isOK(mid, i):
                ok = mid
            else:
                ng = mid
        if ans < i+s[max(0, ok)]:
            ans = i+s[max(0, ok)]

    print(ans)

if __name__ == '__main__':
    main()