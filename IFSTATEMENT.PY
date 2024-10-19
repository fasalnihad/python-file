# score = int(input("enter your score :"))

# if score >= 50:
#     print("you have passed your examination")
#     print("conratulation")
# else:
#     print("you failed in your examination")



mark = int(input("enter your marks:"))




if mark <=100 and mark >=90:
    grade = 'A+'
elif mark <=89 and mark >= 80:
    grade = 'A'
elif mark <=79 and mark >=70:
    grade = 'B'
elif mark <= 69 and  mark >= 60:
    grade = 'C'
elif mark <= 59 and  mark >= 50:
    grade = 'D'
else:
    grade = 'F'


print(f"mark:{mark}\ngrade:{grade}")
if mark >= 50:
    print("you are pass in the exam")
else:
    print("you are failed")

 