# x=10
# if x > 0:
#     print("number is positive")
# elif x < 0:
#     print("the number is negative")
# else:
#     print("number is zero")
    

# x = -1
# if x >= 0:
#     if x > 0:
#         print("number is positive")
#     else:
#         print("number is zero")
# else:
#     print("number is negative")




# marks = (input("enter the marks"))

# # loop through each student's marks

# for  mark in marks:

#     # check the grade based on  marks 

#     if mark >= 90:
#         if mark >90:
#              print("grade A")
#         elif mark >= 80:
#              print("grade B")
#         elif mark >= 70:
#              print("grade C")
#         elif mark >= 60:
#              print("grade D")
#         else:
#              print("grade Fail")


       


#     # check if the students are passed
#           if mark > 50:
#             result = "passed"
#           else:
#             result = "failed"


# List of students' marks
marks = [95, 82, 76, 58, 89, 61, 72, 47]

# Loop through each student's marks
for mark in marks:
    # Check the grade based on the marks
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "Fail"
    
    # Check if the student has passed
    if mark >= 60:
        result = "Passed"
    else:
        result = "Failed"
    
    # Print the result for each student
    print(f"Marks: {mark}, Grade: {grade}, Result: {result}")





    

