#Identifying student grade for each subject
# Marks        Grade
# 92-100         O
# 82-90          A
# 72-80          B
# 62-70          C
# 50-60          D
# less than 50  FAIL
sub1 = int(input("Enter the first sub1 Mark:"))
sub2 = int(input("Enter the second sub2 Mark:"))
sub3 = int(input("Enter the third sub3 Mark:"))
sub4 = int(input("Enter the four sub4 Mark:"))
sub5 = int(input("Enter the five sub5 Mark:"))
sub6 = int(input("Enter the six sub6 Mark:"))
print("\n")
def grade(sub):
 if sub >= 50:
    if sub >=92 and sub <=100 :
        return "O"

    elif sub >=82 and sub <=90:
        return "A"
    elif sub >= 72 and sub <=80:
        return "B"
    elif sub >= 62 and sub <=70:
        return "C"
    else:
        return "D"
 else:
    return "FAIL"
print("  STUDENT GRADE")
print("Subjects     Grade")
print("Subject 1     ",grade(sub1))
print("Subject 2     ", grade(sub2))
print("Subject 3     ", grade(sub3))
print("Subject 4     ", grade(sub4))
print("Subject 5     ", grade(sub5))
print("Subject 6     ", grade(sub6))