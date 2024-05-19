# Define a function named print_fibonacci that takes a single argument 'length'
def print_fibonacci(length):
    # Initialize an empty list to store the Fibonacci sequence
    fibonacci_list = []
    # Initialize two variables 'a' and 'b' to start the sequence
    a, b = 0, 1
    # Loop 'length' times to generate the Fibonacci numbers
    for _ in range(length):  # Using "_" since we don't need to use the loop variable
        # Add the current Fibonacci number 'a' to the list
        fibonacci_list.append(a)
        # Update the variables 'a' and 'b' to generate the next Fibonacci number
        a, b = b, a + b
    # Print the generated Fibonacci sequence list
    print(fibonacci_list)