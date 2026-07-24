def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    
    # dp[i][j]: (i, j) 위치를 우측 하단 꼭짓점으로 하는 가장 큰 빈 정사각형의 한 변의 길이
    dp = [[0] * cols for _ in range(rows)]
    max_square_size = 0  # 공원에 깔 수 있는 가장 큰 정사각형의 한 변 길이
    
    for i in range(rows):
        for j in range(cols):
            # 돗자리를 깔 수 있는 빈 공간("-1")인 경우
            if park[i][j] == "-1":
                # 첫 번째 행이나 첫 번째 열인 경우 최대 길이는 1
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # 현재 위치 기준 위, 왼쪽, 왼쪽 대각선 위를 확인하여 가장 작은 값에 +1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # 공원 내에서 가능한 가장 큰 정사각형 크기 갱신
                max_square_size = max(max_square_size, dp[i][j])
                
    # 지민이가 가진 돗자리 크기를 내림차순(큰 것부터) 정렬
    mats.sort(reverse=True)
    
    # 가장 큰 돗자리부터 차례대로 깔 수 있는지 확인
    for mat in mats:
        if mat <= max_square_size:
            return mat
            
    # 어떤 돗자리도 깔 수 없는 경우
    return -1