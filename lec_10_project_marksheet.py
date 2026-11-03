#Topic--python project Marksheet:

name=input("enter students name:")
roll_no=int(input("enter your roll_no :"))
math=int(input("enter your math marks:"))
science=int(input("enter your science marks:"))
hindi=int(input("enter your hindi marks:"))
sst=int(input("enter your sst marks:"))
english=int(input("enter your english marks:"))


#total and percentage
total_marks=math + hindi+ science+ sst+ math
percentage=total_marks/5

#validation
if math<33 or hindi<33 or science<33 or english<33 or sst<33: 
    result="fail"
    grade="f"
else:
    result="pass"
if percentage>=90:
    grade="A+"
elif percentage>=80:
    grade="A"
elif percentage>=70:
    grade="B+"
elif percentage>=60:
    grade="B"
elif percentage>=50:
    grade="C"
else:
    grade="D"


# Check failed subjects
failed_subjects = []

if math < 33:
    failed_subjects.append("Math")
if science < 33:
    failed_subjects.append("Science")
if english < 33:
    failed_subjects.append("English")
if hindi < 33:
    failed_subjects.append("Hindi")
if sst < 33:
    failed_subjects.append("SST")

# Result and Grade
if len(failed_subjects) > 0:
    result = "Fail"
    grade = "F"
else:
    result = "Pass"
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

# Output
print("\n------ STUDENT MARKSHEET ------")
print("Name:", name)
print("Roll No:", roll_no)
print("Math:", math)
print("Science:", science)
print("English:", english)
print("Hindi:", hindi)
print("SST:", sst)
print("------------------------------")
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Result:", result)
print("Grade:", grade)

# Yeh line sirf fail hone par print hogi
if result == "Fail":
    print("❌ Failed in subjects:", ", ".join(failed_subjects))

print("------------------------------")



#student marksheet caluclator :
name=input("enter your name :")
roll_no=int(input("enter your roll_no:"))
hindi_marks=int(input("enter your hindi_marks:"))
python_marks=int(input("enter your python_marks:"))
english_marks=int(input("enter your english_marks:"))
total_marks=hindi_marks+python_marks
percentage=total_marks/3

print("student name:",name)
print("student roll_no:",roll_no)
print("subject_marks:",hindi_marks)
print("subject_marks:",python_marks)
print("subject_marks:",english_marks)
print("total_marks:",total_marks)
print("percentage:",percentage)
