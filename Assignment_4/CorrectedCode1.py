def evaluate(m1, m2, m3, attendance):
    average = (m1 + m2 + m3) / 3
    if m1 >= 40 and m2 >= 40 and m3 >= 40 and average >= 75 and attendance >= 75:
        return average, "Eligible"
    return average, "Not Eligible"

data = list(map(float, input("Enter marks and attendance: ").split()))
result = evaluate(*data)
print("Average:", result[0])
print("Status:", result[1])
