import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

# 1. 각 위치에서의 '최선의 합'을 저장할 리스트를 만듭니다.
# dp[i]는 i번째 숫자를 마지막으로 포함했을 때 얻을 수 있는 최대 연속합입니다.
dp = [0] * n
dp[0] = num_list[0]

# 2. 두 번째 숫자부터 끝까지 순회합니다.
for i in range(1, n):
    # 핵심 로직: 
    # (이전까지의 합 + 현재 숫자)가 더 큰지, 
    # 아니면 그냥 (현재 숫자)부터 새로 시작하는 게 더 큰지 비교합니다.
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])

# 3. 모든 경우 중 가장 컸던 값을 출력합니다.
print(max(dp))