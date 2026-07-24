import math

def solution(signals):
    # 모든 신호등의 주기(G + Y + R)의 최소공배수(LCM)를 구하여 최대 탐색 시간으로 설정합니다.
    # 제한사항 상 주기의 곱이 크지 않으므로, 안전하게 LCM을 상한선으로 잡습니다.
    lcm_period = 1
    for g, y, r in signals:
        total = g + y + r
        lcm_period = (lcm_period * total) // math.gcd(lcm_period, total)
    
    # 시간은 1초부터 최소공배수 주기까지 탐색
    for t in range(1, lcm_period + 1):
        all_yellow = True
        
        for g, y, r in signals:
            total_cycle = g + y + r
            # 1초부터 시작하므로 인덱스 동기화를 위해 (t - 1) 사용
            remain = (t - 1) % total_cycle
            
            # 노란불 구간: G 이상, G + Y 미만
            if not (g <= remain < g + y):
                all_yellow = False
                break
                
        if all_yellow:
            return t
            
    return -1

# 테스트 예시 출력
print(solution([[2, 1, 2], [5, 1, 1]])) # 결과: 13
print(solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]])) # 결과: 11
print(solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]])) # 결과: -1