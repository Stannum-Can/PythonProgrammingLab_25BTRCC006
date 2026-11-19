marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]

unique_marks = sorted({m for m in marks if m >= 40})
qualified = [m for m in unique_marks if m >= 60]
top_three = qualified[-3:]

print("Processed marks:", unique_marks)
print("Qualified marks:", qualified)
print("Top three:", top_three)
