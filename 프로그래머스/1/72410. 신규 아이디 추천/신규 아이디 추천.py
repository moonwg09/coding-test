import re

def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 치환
    answer = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    answer = re.sub(r'[^a-z0-9\-_.]', '', answer)
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    answer = re.sub(r'\.{2,}', '.', answer)
    
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = re.sub(r'^\.|\.$', '', answer)
    
    # 5단계: 빈 문자열이라면 "a" 대입
    if not answer:
        answer = 'a'
        
    # 6단계: 길이가 16자 이상이면 15자까지 자르고, 끝에 마침표가 있다면 제거
    if len(answer) >= 16:
        answer = answer[:15]
        answer = re.sub(r'\.$', '', answer)
        
    # 7단계: 길이가 2자 이하라면 마지막 문자를 3자가 될 때까지 반복해서 끝에 붙임
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer