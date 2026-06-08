def solution(n, m, section):
    answer = 0
    painted_up_to = 0  # 현재까지 페인트가 칠해진 마지막 구역의 번호
    
    for s in section:
        # 칠해야 할 구역이 아직 칠해지지 않았다면
        if s > painted_up_to:
            # 롤러를 현재 구역부터 칠합니다. (현재 구역 번호 + 롤러 길이 - 1)
            painted_up_to = s + m - 1
            # 페인트칠 횟수 증가
            answer += 1
            
    return answer