a = []
for i in range(2):
    a.append(int(input()))
running = 0
count = 2
while running ==0:
    if a[count-1] <= a[count-2]:
        a.append(a[count-2] - a[count-1])
        count += 1
    else:
        running = 1
print(len(a))