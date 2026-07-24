def solution(s, n):
    answer = []
    for char in s:
        if char.isupper():
            # 대문자 A(65)를 기준으로 이동 후 26으로 나눈 나머지 계산
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer.append(new_char)
        elif char.islower():
            # 소문자 a(97)를 기준으로 이동 후 26으로 나눈 나머지 계산
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer.append(new_char)
        else:
            # 공백은 그대로 유지
            answer.append(char)
            
    return "".join(answer)