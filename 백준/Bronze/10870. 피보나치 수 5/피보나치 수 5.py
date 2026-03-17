#피보나치 수 5

def fibo_r(N):
    # base condition
    if N == 0: return 0
    if N == 1: return 1
    #재귀적인 분해, 조합
    return fibo_r(N-1) + fibo_r(N-2)

N = int(input())
print(fibo_r(N))
    