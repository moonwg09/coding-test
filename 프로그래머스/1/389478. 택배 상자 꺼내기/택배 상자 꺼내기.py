def solution(n, w, num):
    # 0부터 시작하는 index로 변환
    idx = num - 1
    
    # 해당 상자의 층과 열 계산
    r = idx // w
    c = idx % w
    
    # 짝수 층이면 왼쪽->오른쪽(c), 홀수 층이면 오른쪽->왼쪽(w-1-c)
    if r % 2 == 1:
        c = w - 1 - c
        
    count = 0
    # 현재 층보다 위에 있는 같은 열의 상자들을 계산
    # 각 층마다 해당 열에 상자가 있는지 확인 (n개까지)
    for i in range(r + 1, (n + w - 1) // w):
        # i층의 왼쪽->오른쪽, 오른쪽->왼쪽 방향에 따른 해당 열의 실제 인덱스
        if i % 2 == 0:
            target_idx = i * w + c
        else:
            target_idx = i * w + (w - 1 - c)
            
        # 해당 위치에 상자가 존재한다면 카운트
        if target_idx < n:
            count += 1
            
    # 꺼내야 할 상자 본인 포함 (+1)
    return count + 1