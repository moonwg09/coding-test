def solution(number, limit, power):
    # 1부터 number까지 각 숫자의 약수 개수를 저장할 리스트 (0으로 초기화)
    # 인덱스를 맞춰주기 위해 크기를 number + 1로 설정합니다.
    divisors = [0] * (number + 1)
    
    # 1부터 number까지 돌며 각 숫자의 배수에 약수 개수 +1 해주기
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
            
    sum_weight = 0
    # 1번 인덱스부터 끝까지 확인하며 조건에 맞춰 더하기
    for count in divisors:
        if count <= limit:
            sum_weight += count
        else:
            sum_weight += power
            
    return sum_weight