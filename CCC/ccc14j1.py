d1 = int(input())
d2 = int(input())
d3 = int(input())
if d1 + d2 + d3 == 180 and d1 == 60 and d2 == 60 and d3 == 60:
    print("Equilateral")
if d1 + d2 + d3 == 180 and d1 != 60 and (d1 == d2 or d2 == d3 or d3 == d1):
    print("Isosceles")
if d1 + d2 + d3 == 180 and d1 != d2 and d1 != d3 and d3 != d2:
    print("Scalene")
if d1 + d2 + d3!= 180:
    print("Error")