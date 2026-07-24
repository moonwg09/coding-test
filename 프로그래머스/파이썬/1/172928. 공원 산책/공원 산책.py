def solution(park, routes):
    # 공원의 세로(H), 가로(W) 길이
    H = len(park)
    W = len(park[0])
    
    # 1. 시작 지점(S) 찾기
    r, c = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                r, c = i, j
                break
                
    # 2. 이동 방향 정의 (북, 남, 서, 동)
    # y축(행) 이동량, x축(열) 이동량
    moves = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    # 3. 명령에 따라 이동
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        dr, dc = moves[op]
        curr_r, curr_c = r, c
        is_valid = True
        
        # 주어진 칸 수(n)만큼 한 칸씩 이동하며 검증
        for _ in range(n):
            curr_r += dr
            curr_c += dc
            
            # 조건을 위배하면 이동 취소 (공원을 벗어나거나 장애물을 만난 경우)
            if not (0 <= curr_r < H and 0 <= curr_c < W):
                is_valid = False
                break
            if park[curr_r][curr_c] == 'X':
                is_valid = False
                break
                
        # 모든 이동이 무사히 검증되었다면 실제 위치 업데이트
        if is_valid:
            r, c = curr_r, curr_c
            
    return [r, c]