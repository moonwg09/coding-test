def solution(board, h, w):
    # 1. 보드의 길이를 저장할 변수 n 설정
    n = len(board)
    
    # 2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count 초기화
    count = 0
    
    # 3. h와 w의 변화량을 저장할 리스트 (우, 하, 상, 좌 순서)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # 4. 4가지 방향에 대해 반복해서 확인
    for i in range(4):
        # 4-1. 체크할 칸의 좌표 계산
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # 4-2. 계산된 좌표가 보드판의 정상적인 범위 내에 있는지 확인 (0 이상 n 미만)
        if 0 <= h_check < n and 0 <= w_check < n:
            # 4-2-a. 기준 칸의 색과 이웃한 칸의 색이 동일한지 비교
            if board[h][w] == board[h_check][w_check]:
                count += 1
                
    # 5. 최종 카운트 반환
    return count