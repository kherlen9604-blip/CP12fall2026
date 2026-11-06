m = int(input())
d = int(input())
if m < 2 or m == 2 and d < 18:
    print("Before")
if m > 2 or m == 2 and d > 18:
    print("After")
if m == 2 and d == 18:
    print("Special")