def solution(seoul):
    answer = 0
    for index, value in enumerate(seoul):
        if value == "Kim":
            answer = index
    
    return f"김서방은 {answer}에 있다"
    