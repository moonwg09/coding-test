def solution(k, m, score):
    answer = 0
    
    # 1. 사과 점수를 내림차순으로 정렬합니다.
    # 비싼 사과부터 상자에 담아야 이익을 극대화할 수 있습니다.
    score.sort(reverse=True)
    
    # 2. m개씩 묶어서 상자를 만듭니다.
    # 인덱스는 0부터 시작하므로, 각 상자의 가장 낮은 점수의 인덱스는 (m-1), (2m-1), (3m-1)... 이 됩니다.
    for i in range(m - 1, len(score), m):
        # 상자의 가격 = 최저 점수 * m
        answer += score[i] * m
        
    return answer