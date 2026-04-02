
n = int(input())

n5 = n // 5
n3 = n // 3

min_bag = 9999 # 최솟값을 찾기 위해 처음엔 아주 큰 값을 줍니다.
is_found = False

for i in range(n5 + 1):
    for j in range(n3 + 1):
        # n5, n3가 아니라 현재 반복문의 변수인 i와 j를 곱해서 더해야 합니다!
        if i * 5 + j * 3 == n:
            is_found = True
            cur_bag = i + j
            if min_bag > cur_bag:
                min_bag = cur_bag

# 논리를 올바르게 수정: 못 찾았으면(False) -1 출력, 찾았으면 min_bag 출력
if not is_found: 
    print(-1)
else:
    print(min_bag)