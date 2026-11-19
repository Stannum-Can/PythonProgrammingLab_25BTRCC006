def digit_sum(number):
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)

print("Sum of digits:", digit_sum(5824))
print(digit_sum(7), digit_sum(0))
