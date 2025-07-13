
student_marks = {
    "Rohan": 85,
    "Rahul": 78,
    "Adwaith": 92,
    "David": 69,
    "Harry Potter": 88
}


name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
