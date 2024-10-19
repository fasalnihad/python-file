# # def prime_or_not(num):
#     if num < 2:
#         return False
    
#     for i in range(2,int(num ** 0.5)+1):
#         if num % i == 0:
#             return False

#     return True
        
# num = int(input("enter the number"))

# if prime_or_not(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


for num in range(100 , 200):
    if all(num % i == 0 for i in range(2,num)):
        print(num)
