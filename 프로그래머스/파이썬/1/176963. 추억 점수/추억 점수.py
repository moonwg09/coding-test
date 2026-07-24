def solution(name, yearning, photo):
    answer = []
    
    # 1. 이름과 그리움 점수를 딕셔너리로 매핑합니다.
    score_dict = dict(zip(name, yearning))
    
    # 2. 각 사진(행)을 순회하며 점수를 계산합니다.
    for p in photo:
        total_score = 0
        for person in p:
            # 딕셔너리에 이름이 있으면 점수를, 없으면 0을 더합니다.
            total_score += score_dict.get(person, 0)
        
        answer.append(total_score)
        
    return answer