def solution(nums):
    # 1. 내가 가져갈 수 있는 최대 마리 수 (N / 2)
    max_pick = len(nums) // 2
    
    # 2. 연구실에 있는 폰켓몬의 총 종류 수 (중복 제거)
    unique_types = len(set(nums))
    
    # 3. 두 값 중 더 작은 값이 최대로 고를 수 있는 종류의 수가 됩니다.
    return min(max_pick, unique_types)