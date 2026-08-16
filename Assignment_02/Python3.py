# Student Attendance and Performance Monitor

names = ["Anu", "Bharath", "Chitra", "Deepak", "Farah"]

attendance = [92, 68, 85, 45, 78]

marks = [88, 55, 76, 32, 91]

eligible_students = 0

# Process student details using zip() and enumerate()
for student_number, (name, attendance_percentage, mark) in enumerate(
        zip(names, attendance, marks), start=1):

    # Skip invalid attendance or marks
    if (attendance_percentage < 0 or attendance_percentage > 100
            or mark < 0 or mark > 100):
        print(f"{student_number}. Invalid data for {name} - Skipped")
        continue

    # Check examination eligibility
    if attendance_percentage >= 75:

        # Classify marks for eligible students
        if mark >= 80:
            result = "Distinction"
        elif mark >= 60:
            result = "First Class"
        elif mark >= 40:
            result = "Pass"
        else:
            result = "Fail"

        eligible_students += 1

        print(
            f"{student_number}. {name} - "
            f"Attendance: {attendance_percentage}% - "
            f"Marks: {mark} - {result}"
        )

    else:
        print(
            f"{student_number}. {name} - "
            f"Attendance: {attendance_percentage}% - Not Eligible"
        )

print(f"\nTotal Eligible Students: {eligible_students}")
