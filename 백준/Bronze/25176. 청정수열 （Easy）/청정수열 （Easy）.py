import sys
input = sys.stdin.readline

# 1. 입력 받기
    
n = int(input())

# 2. 1부터 n까지 모두 곱하기 (팩토리얼 계산)

answer = 1
for i in range(1, n + 1):
    answer = answer * i

# 3. 결과 출력

print(answer)