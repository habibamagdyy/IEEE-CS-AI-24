def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors

num = int(input("Enter a positive integer: "))

if num < 2:
    print("Please enter a positive integer greater than 1.")
else:
    factors = prime_factors(num)
    print(f"Prime Factors of {num}: {', '.join(map(str, factors))}")
