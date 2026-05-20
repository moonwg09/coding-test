def solution(n):
    answer = ''
    
    # 1. 3진법으로 변환하며 동시에 뒤집기
    while n > 0:
        n, mod = divmod(n, 3) # n을 3으로 나눈 몫과 나머지를 반환
        answer += str(mod)    # 나머지를 문자열로 이어 붙임
        
    # 2. 뒤집힌 3진법 문자열을 다시 10진법 정수로 변환
    return int(answer, 3)