def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# O(n) time | O(n) space
def fibonacci_with_cache(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)
    return cache[n]


# O(n) time | O(1) space
def fibonacci_dp(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


print(fibonacci(7))
print(fibonacci_with_cache(500))
print(fibonacci_dp(500))
