import sys
input = sys.stdin.readline

# 1. 약수를 구하는 함수 (순수하게 약수 리스트만 뱉어냅니다)
def get_divisors(num):
    div_list = []
    for i in range(1, num):
        if num % i == 0:
            div_list.append(i)
    return div_list

# 2. 과잉수인지 판별해주는 함수 (True 또는 False만 뱉어냅니다)
def is_abundant(num):
    div_list = get_divisors(num)
    # 약수들의 합이 자기 자신보다 크면 과잉수(True)
    if sum(div_list) > num:
        return True
    return False

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    
    # 조건 1. 입력받은 n 자체가 과잉수인가?
    if not is_abundant(n):
        print("BOJ 2022")
        
    # n이 과잉수가 맞다면, 조건 2를 검사합니다.
    else:
        # n의 약수 리스트를 가져옵니다.
        divs_of_n = get_divisors(n)
        
        is_beautiful = True  # "모든 약수가 과잉수가 아닐 거야!" 라고 깃발을 듭니다.
        
        for d in divs_of_n:
            # 약수(d) 중 단 하나라도 과잉수라면?
            if is_abundant(d):
                is_beautiful = False  # 깃발을 내립니다.
                break                 # 더 이상 검사할 필요 없이 즉시 탈출!
                
        # 깃발이 끝까지 내려가지 않았다면(True) 아름다운 2022년의 수입니다.
        if is_beautiful:
            print("Good Bye")
        else:
            print("BOJ 2022")