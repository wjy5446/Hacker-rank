import sys

def factorial(n):
    # Complete this function
    if n == 1:
        return n

    return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
