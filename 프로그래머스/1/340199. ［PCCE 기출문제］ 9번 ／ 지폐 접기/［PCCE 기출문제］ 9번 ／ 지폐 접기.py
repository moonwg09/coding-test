def solution(wallet, bill):
    answer = 0
    
    # 지폐의 크기가 지갑 크기에 들어맞을 때까지 반복합니다.
    # 그대로(bill_min <= wallet_min and bill_max <= wallet_max) 들어갈 수 없다면 계속 접어야 합니다.
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        # 항상 길이가 긴 쪽을 반으로 접습니다. (소수점 버림은 // 2 연산 사용)
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        
        # 접은 횟수 증가
        answer += 1
        
    return answer