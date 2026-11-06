B = int(input())
T = int(input())
P = int(input())
Q = T - P - B
if Q < 0:
    print("N")
else:
    print("Y",Q)
