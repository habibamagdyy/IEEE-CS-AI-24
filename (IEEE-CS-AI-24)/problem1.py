numbers = []
while True:
    num = int(input("Enter a number (enter -1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

if numbers:
    largest = max(numbers)
    smallest = min(numbers)
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No numbers were entered.")