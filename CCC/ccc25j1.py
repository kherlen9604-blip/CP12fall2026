N = int(input())
C = int(input())
P = int(input())
Q = N - C * P
if Q > 0:
    print("no")
if Q <= 0:
    print("yes")
