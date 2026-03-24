num1 = int(input())
num2 = int(input())
num3 = int(input())

result = str(num1 * num2 * num3)

# 0이 10개 들어있는 리스트를 만듭니다. (각 칸이 0~9까지 숫자의 개수를 의미)
counts = [0] * 10 

for num in result:
    # 문자를 다시 숫자로 바꿔서(int), 해당 위치의 카운트를 1 올려줍니다.
    # 예: num이 '7'이면 -> counts[7] += 1
    counts[int(num)] += 1

# 리스트에 담긴 개수들을 하나씩 출력
for count in counts:
    print(count)