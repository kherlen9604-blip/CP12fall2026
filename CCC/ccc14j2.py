V = int(input())
S = input()
a = S.count("A")
b = S.count("B")
if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")
