g = input()
g += input()
g += input()
g += input()
g += input()
g += input()
w = g.count("W")
if w ==0:
    print(-1)
elif w<=2:
    print(3)
elif w<=4:
    print(2)
else:
    print(1)