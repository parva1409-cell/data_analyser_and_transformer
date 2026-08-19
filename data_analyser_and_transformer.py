# Data Analyzer and Transformer

data = []


def input_data():
    """Take numbers from the user and store them."""
    global data
    data = list(map(int, input("Enter data(*integers only) separated by spaces: ").split()))
    print("Data stored successfully!")


def summary():
    """Display basic summary of the dataset."""
    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum:", sum(data))
    print("Average:", round(sum(data) / len(data), 2))


def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_data():
    """Filter values using a lambda function."""
    limit = int(input("Enter threshold value: "))
    result = list(filter(lambda x: x >= limit, data))
    print("Filtered Data:", result)


def sort_data():
    """Sort the dataset."""
    choice = input("1. Ascending\n2. Descending\nEnter choice: ")

    if choice == "1":
        print("Sorted Data:", sorted(data))
    elif choice == "2":
        print("Sorted Data:", sorted(data, reverse=True))
    else:
        print("Invalid choice")


def statistics(**kwargs):
    """Return multiple dataset statistics."""
    return kwargs["minimum"], kwargs["maximum"], kwargs["sum"], kwargs["average"]


while True:
    print("\n===== Data Analyzer and Transformer =====")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        if data:
            summary()
        else:
            print("Please enter data first.")

    elif choice == "3":
        n = int(input("Enter a number: "))
        print("Factorial of", n, "is:", factorial(n))

    elif choice == "4":
        if data:
            filter_data()
        else:
            print("Please enter data first.")

    elif choice == "5":
        if data:
            sort_data()
        else:
            print("Please enter data first.")

    elif choice == "6":
        if data:
            minimum = min(data)
            maximum = max(data)
            total = sum(data)
            average = total / len(data)

            a, b, c, d = statistics(
                minimum=minimum,
                maximum=maximum,
                sum=total,
                average=average
            )

            print("\nDataset Statistics:")
            print("Minimum:", a)
            print("Maximum:", b)
            print("Sum:", c)
            print("Average:", round(d, 2))
        else:
            print("Please enter data first.")

    elif choice == "7":
        print("Thank you for using the Data Analyzer!")
        break

    else:
        print("Invalid choice.")