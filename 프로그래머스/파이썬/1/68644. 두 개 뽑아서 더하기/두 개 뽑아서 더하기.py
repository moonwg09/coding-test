from itertools import combinations

def solution(numbers):
    answer = set()
    
    # 1. 서로 다른 인덱스의 2개 숫자를 뽑는 조합 생성
    for a, b in combinations(numbers, 2):
        answer.add(a + b)
        
    # 2. 오름차순 정렬하여 리스트로 반환
    return sorted(list(answer))