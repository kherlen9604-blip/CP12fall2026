d = int(input())
st = 0
while st == 0:
    y = int(input())
    if d > y:
        d += y
    if d <= y:
        print(d)
        st = 1