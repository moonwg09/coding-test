def solution(participant, completion):
    # 1. 빈 딕셔너리(해시 맵)를 생성합니다.
    hash_map = {}
    
    # 2. 참가자 이름을 key로, 등장 횟수를 value로 저장합니다.
    for p in participant:
        if p in hash_map:
            hash_map[p] += 1
        else:
            hash_map[p] = 1
            
    # 3. 완주자 명단을 돌며 딕셔너리에서 횟수를 1씩 차감합니다.
    for c in completion:
        hash_map[c] -= 1
        
    # 4. 여전히 value가 0보다 큰(즉, 1인) 선수가 완주하지 못한 선수입니다.
    for p in hash_map:
        if hash_map[p] > 0:
            return p