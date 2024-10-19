def divide_integer(dividend : int,divisor : int)-> int:
    if divisor ==0:
        return "division by zero is not possible"
    
    quotient = 0
    current_dividend = dividend

    while current_dividend >= divisor:
        current_dividend -= divisor
        quotient += 1
    return quotient

dividend = int(input("enter the number"))
divisor = int(input("enter the divisor"))

print(divide_integer( dividend , divisor))






