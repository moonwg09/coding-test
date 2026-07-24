def solution(s):
    # 길이가 4 또는 6인지 확인
    if len(s) == 4 or len(s) == 6:
        return s.isdigit() # 모든 문자가 숫자로만 구성되어 있으면 True
    return False