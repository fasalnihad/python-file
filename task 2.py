def second_largest(a,b,c):
    x =[a,b,c]
    x.sort()
    return x[1]
input = [[120, 11, 400],[10213, 312, 10],[10, 3, 450]]

for a,b,c in input:
    print(second_largest(a,b,c))
