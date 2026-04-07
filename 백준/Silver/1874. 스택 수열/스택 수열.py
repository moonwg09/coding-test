import sys
input = sys.stdin.readline

N = int(input())
stack = []
operators = []
current = 1  # 다음에 push할 숫자 (1부터 시작)
possible = True

for _ in range(N):
    num = int(input())
    
    while current <= num:
        stack.append(current)
        operators.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        operators.append("-")
    # 3. 일치하지 않으면 만들 수 없는 수열임
    else:
        possible = False
        break

if possible:
    for op in operators:
        print(op)
else:
    print("NO")