# 문자열(N)과 진법(B)을 입력받습니다.
num_str, base = input().split()
base = int(base) # 진법은 계산을 위해 정수로 바꿉니다.

# 이전 문제에서 썼던 36진법 표를 그대로 가져옵니다.
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0

# 계산을 편하게 하기 위해 입력받은 문자열을 뒤집어줍니다. ([::-1] 활용)
# (예: "ZZZ" -> 1의 자리부터 차례대로 계산하기 위함)
num_str = num_str[::-1]

for i in range(len(num_str)):
    # 1. find() 함수를 써서 현재 글자가 표에서 몇 번째(숫자로 얼마)인지 찾습니다.
    value = system.find(num_str[i])
    
    # 2. 값 * (진법의 i제곱)을 계산해서 총합에 더합니다.
    # 파이썬에서 거듭제곱은 ** 기호를 사용합니다.
    total += value * (base ** i)

print(total)