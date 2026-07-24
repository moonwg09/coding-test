def solution(survey, choices):
    # 1. 성격 유형별 점수를 저장할 딕셔너리 초기화
    scores = {char: 0 for char in "RTCFJMAN"}
    
    # 2. 질문들을 순회하며 점수 누적
    for q, choice in zip(survey, choices):
        # 4번(모르겠음)은 점수가 없으므로 스킵
        if choice == 4:
            continue
            
        # 1, 2, 3은 비동의(앞 글자) / 5, 6, 7은 동의(뒷 글자)
        if choice < 4:
            scores[q[0]] += 4 - choice
        else:
            scores[q[1]] += choice - 4
            
    # 3. 4개 지표 순서대로 비교하여 결과 생성
    # 점수가 같으면 사전 순(알파벳 순)이므로 지표를 정렬된 형태로 비교합니다.
    indicators = ["RT", "CF", "JM", "AN"]
    answer = []
    
    for ind in indicators:
        # 두 유형의 점수 비교 (같으면 앞의 글자가 선택되도록 >= 사용)
        if scores[ind[0]] >= scores[ind[1]]:
            answer.append(ind[0])
        else:
            answer.append(ind[1])
            
    return "".join(answer)