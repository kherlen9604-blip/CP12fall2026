n = int(input())
for i in range (n):
    y, m, d = [int(x) for x in input().split()]
    if 2007-y > 18:
        print("Yes")
    elif 2007-y < 18:
        print("No")
    else:
        if m < 2:
            print("Yes")
        elif m > 2:
            print("No")
        else:
            if d < 27:
                print("Yes")
            elif d > 27:
                print("No")
            else:
                print("Yes")