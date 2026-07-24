def solution(s):
    answer = 0
    same_count = 0
    diff_count = 0
    x = ''
    
    for char in s:
        # 새로운 덩어리의 시작점
        if same_count == 0:
            x = char
            same_count = 1
            answer += 1
            continue
            
        # 카운트 비교
        if char == x:
            same_count += 1
        else:
            diff_count += 1
            
        # 두 횟수가 같아지면 초기화
        if same_count == diff_count:
            same_count = 0
            diff_count = 0
            
    return answer