def solution(s):
    stack = []
    answer = True
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        if s[i] == ')' and stack:
            stack.pop()
        elif s[i] == ')' and len(stack) == 0:
            answer = False
    if stack:
        answer = False
    
    return answer