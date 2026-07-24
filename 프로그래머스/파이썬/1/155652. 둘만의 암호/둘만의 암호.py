def solution(s, skip, index):
    # 1. skip에 포함되지 않은 유효한 알파벳 리스트를 만듭니다.
    # 'a'의 아스키 코드는 97, 'z'는 122입니다.
    valid_alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]
    
    # 2. 유효한 알파벳 리스트의 총 길이를 구합니다. (나머지 연산에 사용)
    n = len(valid_alphabets)
    
    # 3. 각 알파벳을 변환하여 결과 문자열을 구성합니다.
    answer = []
    for char in s:
        # 현재 문자의 유효 리스트 내 인덱스를 찾습니다.
        current_idx = valid_alphabets.index(char)
        # index만큼 이동한 후, 리스트 길이를 넘어가면 처음으로 순환하도록 합니다.
        next_idx = (current_idx + index) % n
        # 변환된 문자를 추가합니다.
        answer.append(valid_alphabets[next_idx])
        
    return "".join(answer)