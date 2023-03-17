def sortstring(inp):
    
    inp = inp.split("+")
    inp.sort(key = int)
    return "+".join(inp)
inp = input().strip()
print(sortstring(inp))
