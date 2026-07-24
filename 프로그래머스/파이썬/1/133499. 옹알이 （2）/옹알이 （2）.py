def solution(babbling):
    answer = 0
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 1. 연속되는 발음이 있으면 패스
        if "ayaaya" in word or "yeye" in word or "woowoo" in word or "mama" in word:
            continue
            
        # 2. 가능한 발음을 공백(" ")으로 치환
        for sound in valid_sounds:
            word = word.replace(sound, " ")
            
        # 3. 공백을 모두 제거했을 때 빈 문자열이면 모두 발음 가능한 단어
        if word.strip() == "":
            answer += 1
            
    return answer