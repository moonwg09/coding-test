def solution(friends, gifts):
    # 친구 이름별 인덱스 매핑
    idx = {name: i for i, name in enumerate(friends)}
    n = len(friends)
    
    # 1. 주고받은 선물 기록 (2차원 배열)
    board = [[0] * n for _ in range(n)]
    # 준 선물, 받은 선물 기록
    given = [0] * n
    received = [0] * n
    
    for gift in gifts:
        sender, receiver = gift.split()
        board[idx[sender]][idx[receiver]] += 1
        given[idx[sender]] += 1
        received[idx[receiver]] += 1
        
    # 2. 선물 지수 계산
    gift_index = [given[i] - received[i] for i in range(n)]
    
    # 3. 다음 달에 받을 선물 계산
    next_month = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            # i와 j 사이의 선물 교환 비교
            if board[i][j] > board[j][i]:
                next_month[i] += 1
            elif board[i][j] < board[j][i]:
                next_month[j] += 1
            else:
                # 선물 교환 수가 같으면 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    next_month[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_month[j] += 1
                    
    return max(next_month)