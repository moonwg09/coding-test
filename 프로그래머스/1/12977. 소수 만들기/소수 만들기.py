from itertools import combinations

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    # 2부터 해당 숫자의 제곱근까지 나누어 떨어지는지 확인
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # nums 배열에서 3개를 뽑는 모든 조합을 확인
    for comb in combinations(nums, 3):
        # 3개 숫자의 합이 소수라면 카운트 증가
        if is_prime(sum(comb)):
            answer += 1
            
    return answer