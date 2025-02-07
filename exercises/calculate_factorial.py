# Implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


# Helper method to get and validate a non-negative integer
def get_non_negative_integer():
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            else:
                print("Your number is out of the correct range. Please try again.")
        except ValueError:
            print("Invalid entry. Please try again.")


# Helper method to display the result of a factorial calculation
def display_factorial_results(number, result):
    print(f"The result of {number}! is {result}.")


def main():
    print("Factorial Computation Using Recursion")

    # Get value to calculate, handle negative input
    number = get_non_negative_integer()

    # Call factorial_recursive method
    result = factorial_recursive(number)

    # Display results of the factorial calculation
    display_factorial_results(number, result)


if __name__ == "__main__":
    main()
