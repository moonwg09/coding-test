def fact_r(N):
    # base condition
    if N <= 1: return 1

    # 재귀적인 분해, 조합
    return N * fact_r(N-1)
    
N = int(input())
print(fact_r(N))