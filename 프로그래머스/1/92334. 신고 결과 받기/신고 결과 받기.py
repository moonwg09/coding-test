def solution(id_list, report, k):
    # 1. 유저별 결과 배열의 인덱스를 빠르게 찾기 위한 딕셔너리 생성
    id_idx = {user: i for i, user in enumerate(id_list)}
    
    # 2. 동일한 유저에 대한 중복 신고 제거 (set 활용)
    unique_reports = set(report)
    
    # 3. 각 유저가 누구에게 신고당했는지 기록할 딕셔너리 초기화
    reported_by = {user: [] for user in id_list}
    
    # 4. 신고 내역 순회하며 딕셔너리에 추가
    for r in unique_reports:
        reporter, reportee = r.split()
        reported_by[reportee].append(reporter)
        
    # 5. 메일 수신 횟수를 담을 정답 배열 초기화
    answer = [0] * len(id_list)
    
    # 6. 정지 기준을 만족하는 유저를 찾고, 신고자에게 메일 발송 카운트
    for reportee, reporters in reported_by.items():
        if len(reporters) >= k:  # 정지 기준 횟수를 넘었다면
            for reporter in reporters:
                # 신고자가 id_list의 몇 번째 위치하는지 찾아 1을 더함
                answer[id_idx[reporter]] += 1
                
    return answer