def solution(d, budget):
    d.sort()
    
    answer = 0
    
    for cost in d:
        # 남은 예산으로 현재 부서의 신청 금액을 지원할 수 있는지 확인합니다.
        if budget >= cost:
            budget -= cost  # 예산에서 신청 금액을 차감합니다.
            answer += 1     # 지원한 부서 개수를 1 증가시킵니다.
        else:
            # 예산이 부족해지면 더 이상 지원할 수 없으므로 반복을 종료합니다.
            break
            
    return answer