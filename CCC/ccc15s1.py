k = int(input())
s = []
for i in range(k):
    a = int(input())
    if a != 0:
        s.append(a)
    else:
        s.pop()
print(sum(s))
