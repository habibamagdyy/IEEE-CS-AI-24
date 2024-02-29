def get_numbers():
    while True:
        try:
            numbers = input("Enter a list of numbers separated by space: ").split()
            numbers = [int(num) for num in numbers]
            if len(numbers) < 2:
                raise ValueError("At least 2 numbers are required")
            return numbers
        except ValueError as e:
            print(f"Error: {e}")

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_mean(numbers):
    return sum(numbers) / len(numbers)

def find_mode(numbers):
    mode_dict = {}
    for num in numbers:
        if num in mode_dict:
            mode_dict[num] += 1
        else:
            mode_dict[num] = 1
    max_count = max(mode_dict.values())
    modes = [num for num, count in mode_dict.items() if count == max_count]
    return modes

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return median

def find_range(numbers):
    return find_max(numbers) - find_min(numbers)

def find_variance(numbers):
    mean = find_mean(numbers)
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)
    return variance

def find_STD(numbers):
    variance = find_variance(numbers)
    return variance ** 0.5

def find_Quariles(numbers):
    sorted_numbers = sorted(numbers)
    n = len(numbers)
    Q1 = find_median(sorted_numbers[:n//2])
    Q2 = find_median(sorted_numbers)
    Q3 = find_median(sorted_numbers[n//2:])
    return Q1, Q2, Q3

def find_IQR(numbers):
    Q1, Q2, Q3 = find_Quariles(numbers)
    return Q3 - Q1

def main():
    numbers = get_numbers()
    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", find_mode(numbers))
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_STD(numbers))
    print("Quartiles:", find_Quariles(numbers))
    print("Interquartile Range (IQR):", find_IQR(numbers))

if __name__ == "__main__":
    main()