t=int(input())
s=int(input())
h=int(input())
line = "*" + " "*s +"*"+" "*s +"*"
for i in range(t):
    print(line)
print("*" + "*" * s + "*" + "*" * s + "*")
for i in range(h):
    print(" " * (s+1) + "*")