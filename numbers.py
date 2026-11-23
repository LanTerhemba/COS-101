from collections import Counter

def get_sum(numbers):
    return sum(numbers)

def get_mean(numbers):
    return get_sum(numbers) / len(numbers)

def get_median(numbers):
    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle]
    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

def get_mode(numbers):
    counts = Counter(numbers)
    highest_count = max(counts.values())

    return [number for number, count in counts.items() if count == highest_count]


numbers = []

print("Enter numbers one at a time. Press Enter on a blank line when finished.")

while True:
    user_input = input("Number: ").strip()

    if user_input == "":
        break

    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please enter a valid number.")

if not numbers:
    print("You didn't enter any numbers.")
else:
    print(f"Sum: {get_sum(numbers)}")
    print(f"Mean: {get_mean(numbers)}")
    print(f"Median: {get_median(numbers)}")

    modes = get_mode(numbers)
    if len(modes) == len(set(numbers)):
        print("Mode: There is no mode (all numbers occur equally often).")
    else:
        print(f"Mode: {modes}")
