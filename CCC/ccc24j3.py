n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
biggest = max(s)
while max(s) == biggest:
    s.remove(biggest)
second = max(s)
while second == max(s):
    s.remove(second)
third = max(s)
t = 0
s.append(-1)
while third == max(s):
    s.remove(third)
    t += 1
print(third, t)