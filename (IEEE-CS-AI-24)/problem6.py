num = int(input("Enter a positive integer: "))

if num < 1:
    print("Please enter a positive integer greater than 0.")
else:
    result = (num // 2) * (num // 2 + 1)
    print(f"The sum of even numbers from 1 to {num} is {result}.")
