import matplotlib.pyplot as plt
import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
    memo = {0: 0, 1: 1}
    def fib(n):
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def generate_fibonacci_sequence(n, method='recursive'):
    methods = {'recursive': fibonacci_recursive, 'dynamic': fibonacci_dynamic, 'iterative': fibonacci_iterative}
    return [methods[method](i) for i in range(n)]

def plot_fibonacci(sequence):
    plt.plot(sequence, marker='o', color='b')
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

def time_fibonacci_method(n, method):
    start = time.time()
    generate_fibonacci_sequence(n, method)
    return time.time() - start

def main():
    N = 20
    for method in ['recursive', 'dynamic', 'iterative']:
        sequence = generate_fibonacci_sequence(N, method)
        print(f"{method.capitalize()} first 10: {sequence[:10]}...")
        print(f"Execution time for {method}: {time_fibonacci_method(N, method):.6f} seconds\n")

    plot_fibonacci(generate_fibonacci_sequence(N, 'iterative'))

if __name__ == "__main__":
    main()