def solution(keymap, targets):
    answer = []
    
    # 1. 각 문자의 최소 누름 횟수를 저장할 딕셔너리
    min_press = {}
    
    # 2. keymap을 순회하며 각 문자의 최솟값 갱신
    for key in keymap:
        for idx, char in enumerate(key):
            press_count = idx + 1  # 누름 횟수는 인덱스 + 1
            if char not in min_press:
                min_press[char] = press_count
            else:
                min_press[char] = min(min_press[char], press_count)
                
    # 3. targets의 각 문자열을 만들기 위한 최소 횟수 계산
    for target in targets:
        total_press = 0
        is_possible = True
        
        for char in target:
            if char in min_press:
                total_press += min_press[char]
            else:
                # 자판에 없는 문자가 있다면 작성 불가능
                is_possible = False
                break
        
        if is_possible:
            answer.append(total_press)
        else:
            answer.append(-1)
            
    return answer