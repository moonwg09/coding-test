


n = int(input())

if n % 3 == 0:
    mul = n // 3


count = 0

# 2. x가 1부터 k-2가 될 때까지 반복합니다. 
for x in range(1, mul - 1):
    # x가 정해졌을 때, 남은 값을 y와 z가 나누어 가지는 경우의 수는 (k - x - 1)가지입니다.
    count += (mul - x - 1)

print(count)