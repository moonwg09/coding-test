import sys

# 괄호()를 제거해서 '함수 자체'를 가리키게 합니다.
input = sys.stdin.readline

x_list = []
y_list = []

# 1. 세 점의 좌표를 입력받아 x와 y를 각각 리스트에 담습니다.
for _ in range(3):
    # 이제 input()을 호출하면 sys.stdin.readline()이 실행됩니다.
    line = input().split()
    if not line: break # 혹시 모를 빈 줄 예외 처리
    x, y = map(int, line)
    x_list.append(x)
    y_list.append(y)

# 2. 결과 찾기 (작성하신 로직 그대로)
res_x = 0
res_y = 0
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        res_x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        res_y = y_list[i]

print(res_x, res_y)