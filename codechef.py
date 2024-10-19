t = int(input("enter the number"))

for i in range(t):

    x = int(input("enter the value"))

    if x <=100:
        print(x)
    elif x <= 1000:
        print(x - 25)
    elif x <= 5000:
        print(x - 100)
    else:
        print(x - 500)
    