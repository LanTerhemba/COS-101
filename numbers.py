import statistics

numbers = []


def add_numbers():
    print("Enter numbers one at a time. Press Enter on a blank line when finished.")

    while True:
        user_input = input("Number: ").strip()

        if user_input == "":
            break

        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Please enter a valid number.")


def get_sum(values):
    return sum(values)


def get_mean(values):
    return statistics.mean(values)


def get_median(values):
    return statistics.median(values)


def get_mode(values):
    return statistics.mode(values)


add_numbers()

while True:
    print("\nWhat would you like to find?")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Mode")
    print("5. Add more numbers")
    print("6. Exit")

    choice = input("Choose 1-6: ").strip()

    if choice == "6":
        print("Later!")
        break

    if choice == "5":
        add_numbers()
        continue

    if not numbers:
        print("You haven't entered any numbers yet.")
        continue

    if choice == "1":
        print("Sum:", get_sum(numbers))
    elif choice == "2":
        print("Mean:", get_mean(numbers))
    elif choice == "3":
        print("Median:", get_median(numbers))
    elif choice == "4":
        print("Mode:", get_mode(numbers))
    else:
        print("Please choose a number from 1 to 6.")