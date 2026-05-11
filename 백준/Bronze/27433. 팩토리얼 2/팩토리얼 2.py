def factorial(n, result):
    if n == 1 or n == 0:
        return result

    return factorial(n-1, result * n)

n = int(input())
print(factorial(n, 1))