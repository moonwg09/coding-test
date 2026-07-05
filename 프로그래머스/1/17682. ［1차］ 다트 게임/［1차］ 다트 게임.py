import re

def solution(dartResult):
    # 정규표현식으로 세 세트의 기회를 각각 분리
    # 예: '1S2D*3T' -> [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    scores = pattern.findall(dartResult)
    
    result = []
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    
    for score, bonus, option in scores:
        # 1. 기본 점수 계산 (점수 ^ 보너스)
        curr_score = int(score) ** bonus_dict[bonus]
        
        # 2. 옵션 처리
        if option == '*':
            curr_score *= 2
            # 직전 점수가 있다면 그것도 2배로 만듦
            if result:
                result[-1] *= 2
        elif option == '#':
            curr_score *= -1
            
        result.append(curr_score)
        
    return sum(result)