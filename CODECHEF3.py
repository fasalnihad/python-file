T = int(input("enter the value"))

for i in range(T):
    x,y = map(int, input().split())

    maximum_number_bags = x * y
    bags = maximum_number_bags // 100

    print(bags)

    