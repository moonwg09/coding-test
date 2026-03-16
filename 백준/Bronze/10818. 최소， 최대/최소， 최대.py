# 1. 숫자의 개수를 입력받습니다. (이 문제에서는 사실 리스트의 길이로 알 수 있어서 안 써도 무방하지만 규칙상 받습니다)
num = int(input())

# 2. 한 줄에 입력된 값들을 공백 기준으로 나누고, 모두 정수(int)로 바꿔서 리스트로 만듭니다.
numlist = list(map(int, input().split()))

# 3. 기준점(초기값)은 리스트의 첫 번째 값으로 통일합니다.
min_val = numlist[0]
max_val = numlist[0]


for number in numlist:
    if number < min_val:
        min_val = number
    elif number > max_val:
        max_val = number

# 5. 결과 출력
print(min_val, max_val)