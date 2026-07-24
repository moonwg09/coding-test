def solution(m, n, h, w, drops):
    L = len(drops)
    
    # 빗방울이 떨어지는 시점을 저장하는 Grid (1-based index for drops time)
    # 비가 안 내리는 칸은 L + 1
    time_grid = [L + 1] * (m * n)
    for idx, (r, c) in enumerate(drops):
        time_grid[r * n + c] = idx + 1

    # Parametric Search: K시점까지 떨어진 빗방울을 피할 수 있는가?
    def check(K):
        # K 이하의 시점에 떨어진 빗방울을 1로 표시하는 누적합 배열
        # P[r][c] = (0,0)부터 (r-1, c-1)까지의 빗방울 개수
        P = [0] * ((m + 1) * (n + 1))
        
        # 1. 2D 빗방울 발생 여부 기록 및 누적합
        for r in range(m):
            row_offset = r * n
            p_row_curr = (r + 1) * (n + 1)
            p_row_prev = r * (n + 1)
            
            acc = 0
            for c in range(n):
                if time_grid[row_offset + c] <= K:
                    acc += 1
                P[p_row_curr + c + 1] = P[p_row_prev + c + 1] + acc
        
        # 2. h x w 영역 내 빗방울 수 확인 (0이면 해당 위치 가능)
        # 행/열 순서대로 탐색하여 조건 만족하는 첫 번째 좌표 반환
        for r in range(m - h + 1):
            r1, r2 = r, r + h
            p_r1 = r1 * (n + 1)
            p_r2 = r2 * (n + 1)
            for c in range(n - w + 1):
                c1, c2 = c, c + w
                count = P[p_r2 + c2] - P[p_r1 + c2] - P[p_r2 + c1] + P[p_r1 + c1]
                if count == 0:
                    return True, (r, c)
                    
        return False, None

    # 이진 탐색 범위: 0 ~ L
    # low: 안전하게 비를 안 맞을 수 있는 시점
    low = 0
    high = L
    best_time = 0
    best_pos = (0, 0)

    while low <= high:
        mid = (low + high) // 2
        possible, pos = check(mid)
        if possible:
            best_time = mid
            best_pos = pos
            low = mid + 1
        else:
            high = mid - 1

    # best_time 동안 비를 맞지 않고 버텼다면, best_time + 1 번째 빗방울에 비를 맞게 됨
    # (결과 배치 위치 좌표 반환)
    # best_pos는 이미 가장 위쪽 행, 가장 왼쪽 열 우선 규칙으로 채택됨
    return list(best_pos)