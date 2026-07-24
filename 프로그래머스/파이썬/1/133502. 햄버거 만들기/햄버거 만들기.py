def solution(ingredient):
    answer = 0
    stack = []
    
    for item in ingredient:
        stack.append(item) # 스택에 재료 추가
        
        # 마지막 4개 재료가 [빵, 야채, 고기, 빵] 순서인지 확인
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            # 완성된 햄버거 재료 4개 제거 (뒤에서 4개 추출)
            del stack[-4:]
            
    return answer