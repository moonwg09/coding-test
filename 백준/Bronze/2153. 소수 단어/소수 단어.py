
word = input()

# 인덱스 1이 'a'가 되고, 27이 'A'가 되도록 맨 앞에 쓸데없는 공백(" ")을 하나 끼워줍니다.
letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0  # 내장 함수 sum()과 겹치지 않게 이름 변경

# 1. 점수 계산하기
for ch in word:
    # ch가 letters에서 몇 번째 위치(인덱스)에 있는지 찾아서 바로 더합니다!
    total += letters.index(ch)

# 2. 소수 판별하기 (문제 조건: 1은 소수이므로 is_prime은 기본 True)
is_prime = True

# 1과 자기 자신을 제외한 2부터 total 전까지 나누어 봅니다.
# 만약 total이 1이라면 이 반복문은 아예 실행되지 않고 넘어갑니다. (정상)
for i in range(2, total):
    if total % i == 0:
        is_prime = False
        break

# 3. 결과 출력
if is_prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")

    

        



