import bisect

def solution(message, spoiler_ranges):
    # 1. 메시지에서 단어와 해당 인덱스(시작, 끝) 추출
    words = []
    n = len(message)
    i = 0
    while i < n:
        if message[i] != ' ':
            start = i
            while i < n and message[i] != ' ':
                i += 1
            end = i - 1  # 끝 인덱스 (포함)
            words.append((message[start:i], start, end))
        else:
            i += 1

    # 2. 이진 탐색을 위한 스포 방지 구간의 끝 인덱스 리스트
    re_list = [r[1] for r in spoiler_ranges]
    
    non_spoiler_words = set()
    # 공개 시점(클릭 인덱스)별로 공개되는 단어들을 저장할 딕셔너리
    reveals = {j: [] for j in range(len(spoiler_ranges))}

    # 3. 각 단어가 스포 방지 구간과 겹치는지, 언제 완전히 공개되는지 판별
    for text, ws, we in words:
        # 단어의 시작 인덱스(ws)를 기준으로 이진 탐색하여 겹칠 가능성이 있는 첫 구간 찾기
        idx = bisect.bisect_left(re_list, ws)
        last_overlap = -1
        
        while idx < len(spoiler_ranges):
            rs, re = spoiler_ranges[idx]
            if rs <= we: # 구간의 시작(rs)이 단어의 끝(we)보다 작거나 같으면 겹침
                last_overlap = idx
                idx += 1
            else:
                break
        
        if last_overlap == -1:
            # 어떤 스포 방지 구간과도 겹치지 않음 -> 비 스포일러 단어
            non_spoiler_words.add(text)
        else:
            # 스포 방지 단어이며, 가장 마지막으로 겹치는 구간(last_overlap) 클릭 시 완전 공개됨
            reveals[last_overlap].append(text)

    # 4. 클릭 순서(0 ~ len(spoiler_ranges)-1)대로 중요한 단어인지 판단
    important_count = 0
    seen_spoiler_words = set()

    for j in range(len(spoiler_ranges)):
        for text in reveals[j]:
            # 비 스포일러 구간에 없었고, 이전에 공개된 적도 없는 단어라면 중요한 단어
            if text not in non_spoiler_words and text not in seen_spoiler_words:
                important_count += 1
            
            # 조건 만족 여부와 상관없이, 공개된 스포일러 단어는 기록해 둠 (중복 방지용)
            seen_spoiler_words.add(text)

    return important_count