def solution(cards1, cards2, goal):
    idx1 = 0  # cards1의 현재 인덱스
    idx2 = 0  # cards2의 현재 인덱스
    
    for word in goal:
        # 1. cards1의 범위를 벗어나지 않고, 현재 단어가 cards1의 카드와 일치할 때
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1
        # 2. cards2의 범위를 벗어나지 않고, 현재 단어가 cards2의 카드와 일치할 때
        elif idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1
        # 3. 둘 다 일치하지 않는다면 순서대로 단어를 만들 수 없는 경우임
        else:
            return "No"
            
    return "Yes"