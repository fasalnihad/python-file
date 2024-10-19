import math
t = int(input("enter the number"))

for i in range(t):

    n,x = map(int,input("enter the value").split())

    minumum_number_pizzas = n * x

    total_minimum = math.ceil(minumum_number_pizzas / 4) 

    print(total_minimum)