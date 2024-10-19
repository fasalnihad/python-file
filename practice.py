# mark = int(input("enter your mark"))

# if mark >= 90:
#     grade = "A"
# elif mark >= 80:
#     grade = "B"
# elif mark >= 70:
#     grade = "C"
# elif mark >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"mark :{mark},grade:{grade}")


# checking nested condition

# age = int(input("enter your age"))

# is_student = True

# if age >= 18:
#     print("you are an adult")
#     if is_student:
#         print("you are a student")
#     else:
#         print("you are not student")
# else:
#     print("you are an minor")


# limit = int(input("enter the upper limit numbers: "))
# number = 2

# print(f"prime number upto {limit}")

# is_prime = True

# if number <= 1:
#     is_prime = False
# else:
#     divisor = 2
#     while divisor * divisor <= number:
#         if number % divisor == 0:
#             is_prime = False
#             break
#         divisor +=1

# if is_prime:
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} is not a prime number")

# n = int

# if n % 2 == 0:
#     print("number is even")
# else:
#     print("not even")
    

# name = "hai"
# for i in (100):
#     print("hai")

# i = 1
# while i <= 5:
#     j = 1
#     while j <=5:
#         print("a",end=" ")
#         j = j + 1
#     print()    
#     i = i+1    

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("a",end=" ")
#         j = j +1
#     print()
#     i = i+1 

# i = 1

# while i<= 5:
#     k =1
#     while k <=(5 - i):
#         print(" ",end="")
#         k=k+1
#     j = 1
#     while j <= i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1 


# dict = {"name" : "fasal",
#         "age": 21,
#         "city": "thirurangadi"}
# print(dict)

# Reading from a file
# with open("example.txt", "r") as file:
#     content = file.read()  # Read the entire file
#     print(content)

# # Reading line by line
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Print each line, stripping newline characters

# with open("data.txt","w") as file:
#     file.write("first line\n")
#     file.write("second line\n")

# with open("data,txt","r") as file:
#     content = file.read()
#     print("file content:")
#     print(content)

# #

# for i in range(100,1,-1):
#     print(i)

# list=[]
# for i in range(5):
    # num = int(input("plz enter the numbers  b/w 5 and 25 :"))

    # if num <=25 and num >=5:
    #     list.append(num)
    #     print(list)
    # else:
    #     print("the number is invalid")

# list =[]  
# count = 0
# while True:
#     num = int(input("plz enter the numbers  b/w 5 and 25 :"))

#     if num <=25 and num >=5:
#         list.append(num)
#         count = count + 1
#     else:
# #         print("the number is invalid")
# #     if count >= 5:
# #         break
# # print(list)
# s = set(input("enter the names"))
# length=len(s)
# print(length)

f =2 * 2 * 2*2*2*2*2*2*2*2
print(f)