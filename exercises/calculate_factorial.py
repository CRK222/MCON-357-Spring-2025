# Iterative factorial method
def factorial_iterative(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


# Implement factorial_recursive method
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


# Implement factorial_recursive, but solving the issue of recursion limit
def factorial_iterative_recursive(number):
    stack = []
    result = 1

    while number > 1:
        stack.append(number)
        number -= 1

    while stack:
        result *= stack.pop()

    return result


# Helper method to validate a non-negative integer
def process_input(user_input):
    try:
        num = int(user_input)
        if num >= 0:
            return num, False, None
        else:
            return None, True, "Your number is out of the correct range. Please try again."
    except ValueError:
        return None, True, "Invalid entry. Please try again."


# Helper method to display the result of a factorial calculation
def display_factorial_results(number, result):
    print(f"The result of {number}! is {result}.")


def main():
    print("Factorial Computation Using Recursion")
    number = 0

    user_input = input("Enter a non-negative integer: ")

    # Get value to calculate, print message if errors
    repeat_loop = True
    while repeat_loop:
        number, repeat_loop, error_msg = process_input(user_input)

        if error_msg is not None:
            print(error_msg)
            user_input = input("Enter a non-negative integer: ")

    # Call factorial_recursive method
    result = factorial_recursive(number)

    # Display results of the factorial calculation
    display_factorial_results(number, result)


if __name__ == "__main__":
    main()
