m = input()
h = m.count(":-)")
s = m.count(":-(")
if h > s:
    print("happy")
elif s > h:
    print("sad")
elif h == 0 and s == 0:
    print("none")
else:
    print("unsure")