def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        # 출근 희망 시각을 시간(h)과 분(m)으로 분리
        h = schedules[i] // 100
        m = schedules[i] % 100
        
        # 인정 종료 시각을 분 단위로 계산
        limit_minutes = (h * 60 + m) + 10
        
        is_eligible = True
        for day_idx in range(7):
            # 현재 요일 계산 (1:월, ..., 6:토, 7:일)
            current_day = (startday + day_idx - 1) % 7 + 1
            
            # 토요일(6), 일요일(7)은 제외
            if current_day == 6 or current_day == 7:
                continue
            
            # 실제 출근 시각을 분 단위로 변환
            actual_h = timelogs[i][day_idx] // 100
            actual_m = timelogs[i][day_idx] % 100
            actual_minutes = actual_h * 60 + actual_m
            
            # 인정 시간보다 늦게 출근했다면 지각
            if actual_minutes > limit_minutes:
                is_eligible = False
                break
        
        if is_eligible:
            answer += 1
            
    return answer