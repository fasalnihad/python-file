def second_largest(A, B, C):
    numbers = [A, B, C]
    numbers.sort() 
    return numbers[1] 
inputs = [
    [120, 11, 400], [10213, 312, 10],   [10, 3, 450]]
for a, b, c in inputs:
    print(second_largest(a,b,c))



