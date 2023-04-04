n = int(input())
s = input()
add = 0
for char in s:
    if char == "-":
        add -= 1
    elif char == "+":
        add += 1
    if add < 0:
        add = 0
print(add)
