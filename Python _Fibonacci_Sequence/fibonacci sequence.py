def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        print("❌ Please enter a positive integer.")
        return
    
    fib_sequence = [0, 1]  # First two terms

    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Sum of last two numbers

    print("🔢 Fibonacci Sequence:", *fib_sequence)

# Taking user input
try:
    terms = int(input("Enter the number of terms: "))
    fibonacci(terms)
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
