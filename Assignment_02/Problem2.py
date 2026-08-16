n = int(input("Enter number of consumers: "))

output = []

for i in range(1, n + 1):
    name = input(f"Consumer {i}: ")
    units = int(input("Units: "))

    if units < 0:
        output.append(f"Invalid units for {name} - Skipped")
        continue

    if units == 0:
        output.append("0 units entered. Processing stopped.")
        break

    if units <= 100:
        rate = 2
    elif units <= 200:
        rate = 3
    elif units <= 300:
        rate = 5
    else:
        rate = 7

    bill = units * rate
    output.append(f"{name} - {units} units - Bill: ₹{bill}")

print()
print("\n".join(output))
