def solution(lottos, win_nums):
    # 1. 확실하게 맞춘 번호의 개수와 0의 개수를 구합니다.
    # set(집합)을 활용하면 교집합(&)으로 빠르게 일치하는 개수를 찾을 수 있습니다.
    match_count = len(set(lottos) & set(win_nums))
    zero_count = lottos.count(0)
    
    # 2. 맞춘 개수에 따른 순위를 매핑하는 딕셔너리 또는 리스트를 만듭니다.
    # index가 맞춘 개수, value가 순위입니다. (0개나 1개 맞추면 모두 6등)
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    # 3. 최고 순위와 최저 순위를 계산합니다.
    max_rank = rank[match_count + zero_count]
    min_rank = rank[match_count]
    
    return [max_rank, min_rank]