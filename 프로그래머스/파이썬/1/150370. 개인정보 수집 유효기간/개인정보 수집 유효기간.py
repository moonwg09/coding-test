def solution(today, terms, privacies):
    # 1. 오늘 날짜를 일 단위로 변환
    y, m, d = map(int, today.split('.'))
    today_total_days = y * 12 * 28 + m * 28 + d
    
    # 2. 약관 정보를 딕셔너리로 저장
    term_dict = {}
    for term in terms:
        name, duration = term.split()
        term_dict[name] = int(duration) * 28
        
    result = []
    
    # 3. 각 개인정보 파기 여부 확인
    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        y, m, d = map(int, date.split('.'))
        
        # 수집 날짜를 일 단위로 변환
        collect_total_days = y * 12 * 28 + m * 28 + d
        
        # 유효기간 만료일 계산
        expiry_date = collect_total_days + term_dict[term_type]
        
        # 만료일이 오늘 날짜보다 작으면 파기 대상
        if expiry_date <= today_total_days:
            result.append(i + 1)
            
    return result