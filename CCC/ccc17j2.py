N=int(input())
K=int(input())
R=0
O=0
for i in range(K+1):
    O+=N*(10**R)
    R+=1
print(O)