def solution(a, b):
    # 2016년 각 달의 일수 (윤년이므로 2월은 29일)
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 1월 1일이 금요일(FRI)이므로, 0일째(자기자신)가 FRI가 되도록 배열 구성
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월부터 a-1월까지의 일수를 모두 더하고 b-1일을 더함
    total_days = sum(months[:a-1]) + (b - 1)
    
    # 7로 나눈 나머지를 인덱스로 사용
    return days[total_days % 7]

# 테스트
print(solution(5, 24))  # 출력: "TUE"