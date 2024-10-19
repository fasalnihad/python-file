# def calculate_grade(score):
#     if >= 90:
#         return "A"
#     elif >= 80:
#         return "B"
#     elif >= 70:
#         return "c"
#     elif >= 60:
#         return "D"
#     else:
#         return "F"
    
# score = calculate_grade(score)

# print(f"the grade is: {score}")

# caluculate_grade(score):

def calculate_grade():
    score = int(input("enter the score (0-100):"))

    if score < 0 or score > 100:
        print("invalid score,please enter a score between 0 and 100")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"score:{score},grade:{grade}")
calculate_grade()