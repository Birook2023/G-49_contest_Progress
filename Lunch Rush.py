n, k = list(map(int, input().split()))
res = []
while n:
    fi, ti = list(map(int, input().split()))
    if ti > k:
        res.append(fi - (ti - k))
    else:
        res.append(fi)
    n -= 1
print(max(res))
