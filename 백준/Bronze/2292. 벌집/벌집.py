n = int(input())

# 시작점(1번 방)의 기본 세팅
honeycomb = 1  # 각 겹의 마지막 방 번호 (초기값 1겹의 마지막 번호는 1)
layer = 1      # 현재 몇 겹째인지 (초기값 1겹)

# 입력받은 n이 현재 겹의 마지막 방 번호(honeycomb)보다 클 때까지 반복
while n > honeycomb:
    honeycomb += 6 * layer  # 다음 겹의 마지막 방 번호로 업데이트 (6, 12, 18...씩 더해짐)
    layer += 1              # 겹 수(지나가는 방의 수) 1 증가

print(layer)