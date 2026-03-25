def fibonacci(n):                                                   # Fn = Fn-1+ Fn-2
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)