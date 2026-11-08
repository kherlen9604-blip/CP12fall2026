n = int(input())
pa = 100
pb = 100
for i in range(n):
    ra,rb = [int(x) for x in input() . split()]
    if ra > rb:
        pb -= ra
    elif ra == rb:
        ra = ra
    else:
        pa -= rb
print(pa)
print(pb)