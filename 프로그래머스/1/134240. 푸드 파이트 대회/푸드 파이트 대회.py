def solution(food):
    left_side = ""
    
    # 1번 음식부터 차례대로 확인 (food[0]은 물이므로 제외)
    for i in range(1, len(food)):
        # 해당 음식을 한 선수가 먹을 수 있는 양만큼 문자열에 추가
        left_side += str(i) * (food[i] // 2)
        
    # 왼쪽 배치 + 물(0) + 오른쪽 배치(왼쪽 배치를 뒤집은 것)
    return left_side + "0" + left_side[::-1]