def solution(number):
    answer = 0
    n = len(number)
    
    # 서로 다른 3명의 학생을 고르는 3중 반복문
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 세 학생의 번호 합이 0이면 삼총사 카운트 증가
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
                    
    return answer