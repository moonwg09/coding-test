import sys

# 이제부터 input()을 호출하면 실제로는 sys.stdin.readline()이 동작합니다.
# 속도가 훨씬 빨라져서 "시간 초과" 예방에 아주 좋습니다.
input = sys.stdin.readline

while True:
    # 1. 문장 읽기: .rstrip('\n')을 써서 줄바꿈 문자만 제거합니다.
    # 입력을 빠르게 받기 위해 선언한 input()을 사용합니다.
    line = input().rstrip('\n')
    
    # 2. 종료 조건: 마침표 하나만 들어오면 무한 루프를 탈출합니다.
    if line == ".":
        break
    
    stack = []          # 괄호 짝을 맞추기 위한 스택(바구니)
    is_balanced = True  # 균형이 맞는지 확인할 변수 (기본값은 True)
    
    # 3. 문장의 문자들을 하나씩 확인합니다.
    for char in line:
        # (1) 열린 괄호 '(', '['를 만나면 스택에 추가합니다.
        if char == '(' or char == '[':
            stack.append(char)
        
        # (2) 소괄호 닫기 ')'를 만난 경우
        elif char == ')':
            # 스택이 비어있지 않고, 맨 위(최근 것)가 '('라면 짝이 맞습니다.
            if stack and stack[-1] == '(':
                stack.pop() # 짝이 맞으므로 꺼냅니다.
            else:
                is_balanced = False # 스택이 비었거나 짝이 안 맞으면 실패!
                break # 더 볼 것도 없이 루프 중단
                
        # (3) 대괄호 닫기 ']'를 만난 경우
        elif char == ']':
            # 스택이 비어있지 않고, 맨 위(최근 것)가 '['라면 짝이 맞습니다.
            if stack and stack[-1] == '[':
                stack.pop() # 짝이 맞으므로 꺼냅니다.
            else:
                is_balanced = False # 실패!
                break
    
    # 4. 최종 판정
    # 모든 글자를 확인했는데 '실패 깃발'이 없고, '스택이 텅 비어'있어야 합니다.
    # (스택에 괄호가 남아있다면 닫히지 않은 괄호가 있다는 뜻이니까요.)
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")