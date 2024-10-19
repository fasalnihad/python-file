# t = int(input("enter the number"))

# for i in range(t):
#     b1,b2,b3 = int(input("enter the number").split())

#     if b1 == 0 and b2 == 1 and b3 ==0:
#         print("water filling  time")
#     else:
#         print("not now")

t = int(input("enter the number"))

for i in range(t):

    b1,b2,b3 = map(int,input("enter the values").split())

    count_list = [b1,b2,b3].count(0)

    if count_list >= 2:
        print("water filling time")
    else:
        print("Not Now")



