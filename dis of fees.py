# str1 = "fasal "
# str2 = "nihad"
# print(str1 + str2)

# fees and discount are given
fees = int(input("enter your fees : "))

discount_percent = int(input("enter your percent : "))


# here calculating the discount of amount

discount_amount = discount_percent / 100 * fees

# finding the discount of fees

discount_fees = fees - discount_amount

# printing the discount of fees

print("fees is discounted : ",discount_fees)

