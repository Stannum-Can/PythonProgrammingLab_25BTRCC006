# Student Result Analyzer

names = ["Arun", "Bala", "Charan", "Divya", "Esha"]
marks = [85, 72, 38, 105, 91]

valid_students = 0

# Process student names and marks together
for student_number, (name, mark) in enumerate(zip(names, marks), start=1):

    # Skip invalid marks
    if mark < 0 or mark > 100:
        print(f"Invalid marks for {name} - Skipped")
        continue

    # Classify student based on marks
    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    elif mark >= 40:
        result = "Average"
    else:
        result = "Fail"

    valid_students += 1

    print(f"{student_number}. {name} - {mark} - {result}")

print(f"\nTotal Valid Students: {valid_students}")
