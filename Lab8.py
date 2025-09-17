def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

def fibonacci(n):
    if n < 0:
        return "Fibonacci is not defined for negative numbers"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print("Fibonacci of 6:", fibonacci(6))
