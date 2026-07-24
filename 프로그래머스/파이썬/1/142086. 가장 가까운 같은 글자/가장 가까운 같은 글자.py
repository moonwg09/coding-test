def solution(s):
    answer = []
    # 각 글자의 가장 최근 등장 위치를 저장할 딕셔너리
    last_position = {}
    
    for i, char in enumerate(s):
        if char in last_position:
            # 이전에 나온 적이 있다면, 현재 인덱스(i)에서 직전 인덱스를 빼줍니다.
            answer.append(i - last_position[char])
        else:
            # 처음 나온 글자라면 -1
            answer.append(-1)
        
        # 현재 글자의 위치를 최신 상태로 업데이트
        last_position[char] = i
        
    return answer