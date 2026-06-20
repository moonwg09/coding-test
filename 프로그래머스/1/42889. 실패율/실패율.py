def solution(N, stages):
    answer = []
    
    # 1. 총 플레이어 수
    total_players = len(stages)
    
    # 2. 각 스테이지별 머물고 있는 플레이어 수 카운트
    # 스테이지 번호는 1부터 N+1까지 있으므로 크기가 N+2인 리스트를 생성합니다.
    stage_counts = [0] * (N + 2)
    for stage in stages:
        stage_counts[stage] += 1
        
    # 3. 각 스테이지별 실패율 계산
    failure_rates = []
    for i in range(1, N + 1):
        if total_players > 0:
            # 실패율 계산: 현재 스테이지에 머무는 사람 / 도달한 사람
            fail_rate = stage_counts[i] / total_players
            # 다음 스테이지 도달자 수 계산 (현재 스테이지에 머무는 사람 제외)
            total_players -= stage_counts[i]
        else:
            # 스테이지에 도달한 유저가 없는 경우 실패율은 0
            fail_rate = 0
            
        failure_rates.append((i, fail_rate))
        
    # 4. 정렬 조건에 맞게 정렬
    # x[1] (실패율) 기준 내림차순(-), x[0] (스테이지 번호) 기준 오름차순(+)
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 5. 정렬된 결과에서 스테이지 번호만 추출
    answer = [stage for stage, rate in failure_rates]
    
    return answer