D = int(input())
E = int(input())
for i in range(E):
    sign=input()
    Q=int(input())
    if sign=="+":
        D+=Q
    else:
        D-=Q
print(D)