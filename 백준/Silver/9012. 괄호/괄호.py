T = int(input())

for _ in range(T):
    stack = []
    isVPS = "YES"

    PS = list(input()) #list로 변환하면 "abc" 를 "a", "b", "c"로 바꿔준다
    for p in PS:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if stack:
                stack.pop()
            else:
                isVPS = 'NO'
                break
    
    if stack:
        isVPS = 'NO'
        
    print(isVPS)