def solution(s):
    words = s.split(" ")
    jadencase_words = []
    
    for word in words:
        # 연속된 공백 때문에 빈 문자열('')이 들어올 수 있으므로 체크해야 합니다!
        if word == "": 
            jadencase_words.append("")
        else:
            # 첫 글자는 대문자로, 나머지(인덱스 1부터 끝까지)는 소문자로 변환해서 합침
            changed_word = word[0].upper() + word[1:].lower()
            jadencase_words.append(changed_word)
            
    return " ".join(jadencase_words)
