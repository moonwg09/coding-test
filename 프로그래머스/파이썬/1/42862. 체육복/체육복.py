def solution(n, lost, reserve):
    # 1. 여벌이 있는데 도난당한 학생을 먼저 제외합니다. (차집합)
    # set을 사용하면 O(1) 연산이 가능하고 중복 제거에 효율적입니다.
    actual_reserve = list(set(reserve) - set(lost))
    actual_lost = list(set(lost) - set(reserve))
    
    # 2. 정렬 (번호 순서대로 처리해야 최적의 선택을 할 수 있습니다)
    actual_reserve.sort()
    actual_lost.sort()
    
    # 3. 빌려줄 수 있는 학생이 앞번호 먼저, 그다음 뒷번호 학생에게 빌려줍니다.
    for r in actual_reserve:
        if r - 1 in actual_lost:
            actual_lost.remove(r - 1)
        elif r + 1 in actual_lost:
            actual_lost.remove(r + 1)
            
    # 4. 전체 학생 수에서 여전히 체육복이 없는 학생 수를 뺍니다.
    return n - len(actual_lost)