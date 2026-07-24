def solution(n):
    answer = 0
    
    # 1부터 n까지의 자연수 중 홀수인 약수의 개수를 구합니다.
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            answer += 1
            
    return answer