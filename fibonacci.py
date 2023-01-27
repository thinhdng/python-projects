

def fibonacci(n):
    if(n <= 1):
        return n  
    #recursion using the formula fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(15))