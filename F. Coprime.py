import math
t = int(input())
while t:
    
    n = int(input())
    a = list(map(int, input().split()))
    res = -1
    dic = {}
    for i in range(n):
        dic[a[i]] = i + 1
    for i in dic:
        for j in dic:
            if math.gcd(i,j) == 1 and (dic[i] + dic[j]) > res:
                res = dic[i] + dic[j]
    print(res)
    
    t -= 1
