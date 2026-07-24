def solution(sizes):
    max_w = 0  # 가장 긴 가로 길이를 담을 변수
    max_h = 0  # 가장 긴 세로 길이를 담을 변수
    
    for w, h in sizes:
        # 두 길이 중 큰 값을 가로(rotated_w), 작은 값을 세로(rotated_h)로 둡니다.
        rotated_w = max(w, h)
        rotated_h = min(w, h)
        
        # 지금까지의 최댓값과 비교하여 갱신합니다.
        max_w = max(max_w, rotated_w)
        max_h = max(max_h, rotated_h)
        
    return max_w * max_h