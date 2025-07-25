#Student Details
student_id=66
student_name="Yeswanth"
student_age=22
#Scores Details
quiz_score=80
assignment_score=95
exam_score=90
#Attendance Details
student_attendence =89
#use arithmetic operators to calculate
total_score= quiz_score + assignment_score + exam_score
average_score= total_score/3
#use relational operators to determine
is_passed =average_score>=75
#use increment operator to update
student_attendence+=1
#use logical operations to determine award eligibility
qualified_award=student_attendence>+90 and is_passed
print(f"Student ID:{student_id}")
print(f"Student Name:{student_name}")
print(f"Student Age:{student_age}")
print(f"Total Score:{total_score}")
print(f"Average Score:{average_score}")
print(f"Current Attendence:{student_attendence}" )
print(f"Student Passed:{is_passed}")
print(f"Student Qualified:{qualified_award}")