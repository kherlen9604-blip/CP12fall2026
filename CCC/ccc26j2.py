a = []
for i in range(5):
    a.append(int(input()))
b = int(input())
a.sort()
a.pop(0)
a.pop(3)
print(sum(a) * b)