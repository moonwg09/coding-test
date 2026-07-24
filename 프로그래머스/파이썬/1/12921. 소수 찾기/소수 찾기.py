def solution(n):
    # 0부터 n까지의 리스트를 만들고, 처음엔 모두 소수(True)라고 가정합니다.
    sieve = [True] * (n + 1)
    
    # 0과 1은 소수가 아니므로 False로 설정합니다.
    sieve[0] = False
    sieve[1] = False
    
    # n의 최대 약수가 sqrt(n) 이하이므로 그까지만 검사하면 됩니다.
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수라면
            # i의 배수들을 모두 소수가 아닌 것(False)으로 지웁니다.
            for j in range(i * i, n + 1, i):
                sieve[j] = False
                
    # True로 남아있는 값들의 개수(소수의 개수)를 반환합니다.
    return sieve.count(True)