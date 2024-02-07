def is_perfect_number(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum == num

num = int(input("Enter a positive integer: "))

if num < 1:
    print("Please enter a positive integer greater than 0.")
else:
    if is_perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
