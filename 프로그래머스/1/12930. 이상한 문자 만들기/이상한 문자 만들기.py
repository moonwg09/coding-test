def solution(s):
    words = s.split(" ") # 공백을 기준으로 단어를 나눕니다.
    converted_words = []
    
    for word in words:
        new_word = ""
        for i in range(len(word)):
            # 짝수번째 인덱스 문자는 대문자로, 홀수번째는 소문자로
            if i % 2 == 0:
                new_word += word[i].upper() 
            else:
                new_word += word[i].lower()
        converted_words.append(new_word)
        
    # 변환된 단어들을 다시 공백으로 합칩니다.
    return " ".join(converted_words)