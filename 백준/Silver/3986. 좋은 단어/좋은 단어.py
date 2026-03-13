
N = int(input())

count = 0

for _ in range(N):

    line = input()
    stack = []
    for char in line:
        if char == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(char)
        
        if char == 'B':
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append(char)
    if not stack:
        count += 1

print(count)



