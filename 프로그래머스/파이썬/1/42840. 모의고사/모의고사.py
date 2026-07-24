def solution(answers):
    # 1. 수포자들의 찍기 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 2. 맞힌 문제 수를 저장할 리스트 (수포자 1, 2, 3 순서)
    scores = [0, 0, 0]
    
    # 3. 정답 채점하기
    for idx, answer in enumerate(answers):
        if answer == p1[idx % len(p1)]:
            scores[0] += 1
        if answer == p2[idx % len(p2)]:
            scores[1] += 1
        if answer == p3[idx % len(p3)]:
            scores[2] += 1
            
    # 4. 가장 높은 점수 찾기
    max_score = max(scores)
    
    # 5. 최고 득점자 선별 (인덱스가 0부터 시작하므로 +1)
    result = []
    for idx, score in enumerate(scores):
        if score == max_score:
            result.append(idx + 1)
            
    return result