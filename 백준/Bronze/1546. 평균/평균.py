# 입력 속도를 높이는 sys.stdin.readline은 잘 쓰셨습니다!
import sys
input = sys.stdin.readline

count = int(input())

# 1. 점수들이 한 줄에 띄어쓰기로 들어오므로 split()을 써서 한 번에 리스트로 만듭니다.
score = list(map(int, input().split()))

# 파이썬의 max() 함수를 쓰면 정렬(sort)을 안 해도 최댓값을 바로 찾아줍니다!
max_score = max(score)
total = 0

# 2. 모든 점수에 대해 똑같은 공식을 적용합니다. (if문 불필요)
for number in score:
    # 현재 점수 / 최댓값 * 100 을 바로 total에 더해줍니다.
    total += (number / max_score) * 100

# 3. 새로운 점수들의 총합을 과목 수로 나누어 평균을 출력합니다.
print(total / count)


