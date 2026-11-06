limit = int(input())
speed = int(input())
o = speed - limit
if o <= 0:
    print("Congratulations, you are within the speed limit!")
elif o <= 20:
    print("You are speeding and your fine is $100.")
elif o <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")