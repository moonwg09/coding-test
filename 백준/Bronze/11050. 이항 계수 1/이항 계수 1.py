
n, k = map(int, input().split())


def factorial (num):
    total = 1
    for i in range(1, num+1):
        total *= i
    
    return total

Binomial = factorial(n) // (factorial(k) * factorial((n-k)))

print(Binomial)
