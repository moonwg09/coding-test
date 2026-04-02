
# t = int(input())

# total = 1

# for _ in range(t):
#     fac = int(input())

# for i in range(1,fac+1):
#     total *= i

# total_list = list(str(total))

# for _ in total_list:
#     if total_list[-1] == '0':
#         del(total_list[-1])

# print(total_list[-1])

t = int(input())

for _ in range(t):
    fac = int(input())
    
    # 1. 매 테스트 케이스마다 total을 1로 새롭게 초기화!
    total = 1

    # 2. 계산과 출력 모두 테스트 케이스 반복문 안으로 들여쓰기!
    for i in range(1, fac + 1):
        total *= i

    total_list = list(str(total))

    # 3. for문 대신 while문 사용: "맨 뒤가 '0'이면 계속 지워라"
    while total_list[-1] == '0':
        total_list.pop()  # 맨 뒤의 요소를 깔끔하게 제거해 주는 함수입니다.

    print(total_list[-1])
