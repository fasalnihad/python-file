
# MAHASENA QUESTION

n = (input("enter the value").split(" "))

count = 0
for i in n:
    if int(i)%2==0:
        count += 1
    else:
        count -= 1
if count > 0:
    print("ready for battle")
else:
    print("Not Ready")