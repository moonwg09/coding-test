def solution(players, callings):
    # 선수의 이름: 현재 등수(인덱스)를 저장하는 딕셔너리 생성
    player_indices = {player: i for i, player in enumerate(players)}
    
    for called_player in callings:
        # 1. 추월한 선수의 현재 위치(인덱스)
        current_idx = player_indices[called_player]
        # 2. 바로 앞 선수의 위치
        front_idx = current_idx - 1
        # 3. 바로 앞 선수의 이름
        front_player = players[front_idx]
        
        # 4. players 배열에서 두 선수의 위치 스왑(Swap)
        players[current_idx], players[front_idx] = players[front_idx], players[current_idx]
        
        # 5. 딕셔너리(해시 맵)의 등수 정보도 업데이트
        player_indices[called_player] = front_idx
        player_indices[front_player] = current_idx
        
    return players