def generate_primes(start, end):
    primes = []
    for number in range(max(start, 2), end + 1):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            primes.append(number)
    return primes

print(generate_primes(1, 30))
print(generate_primes(2, 2))
print(generate_primes(14, 16))
