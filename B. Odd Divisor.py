t = int(input())
 
while t:
    n = int(input())
    res = "yes"
    if n % 2 != 0:
        print("yes")
    else:
        while n % 2 == 0:
            n /= 2   
            if n <= 1:
               res = "no"
    
        print(res)
    t -= 1
