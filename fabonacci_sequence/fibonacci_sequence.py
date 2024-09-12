def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the nth number.
    :param n: The number of Fibonacci numbers to generate.
    :return: A list of Fibonacci numbers up to the nth number.
    """
    # Base cases for n = 0 or 1
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    
    # Start with the first two numbers
    fib_sequence = [0, 1]
    
    # Generate the rest of the sequence
    for i in range(2, n):
        next_fib= fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Example: Generate the first 11 Fibonacci numbers
n = 1
sequence = fibonacci_sequence(n)
print(sequence)
