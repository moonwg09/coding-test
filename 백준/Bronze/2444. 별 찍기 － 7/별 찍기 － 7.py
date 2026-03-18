import sys

# N을 입력받습니다.
n = int(sys.stdin.readline())

# 1. 상단부 (1번째 줄부터 N번째 줄까지)
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 2. 하단부 (N-1번째 줄부터 1번째 줄까지 역순)
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))