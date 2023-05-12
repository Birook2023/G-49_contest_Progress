t = int(input())
 
while t:
    n = int(input())
    a = list(map(int, input().split()))
    res, i = 0, 0
    
    while i < n:
        res |= a[i]
        i += 1
    print(res)
    
    t -= 1
