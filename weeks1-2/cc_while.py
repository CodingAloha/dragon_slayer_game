
x = 0

while x != 10:
    x = x + 1
    if x < 5:
        print(x)
    elif x == 6:
        print(x)
        continue
    elif x >= 5 and x <= 8:
        print("x is bigger then or equal to 5, and less then or equal to 8, but not 6. It is:", x)
    else:
        print("x is bigger than 8. It is:", x)
