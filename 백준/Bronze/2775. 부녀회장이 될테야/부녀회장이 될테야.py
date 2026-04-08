T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    # 1. 0층의 거주민 수 리스트를 만듭니다. (1호부터 n호까지)
    # 예: n이 4라면 people = [1, 2, 3, 4]
    people = [i for i in range(1, n + 1)]
    
    # 2. 1층부터 k층까지 차례대로 층을 쌓아 올립니다.
    for _ in range(k):
        # 3. 1호(인덱스 0)는 항상 1명이므로, 2호(인덱스 1)부터 계산합니다.
        for j in range(1, n):
            # 핵심 규칙: (새로운 내 방 인원) = (옆방 인원) + (원래 적혀있던 아래층 내 방 인원)
            people[j] = people[j] + people[j - 1]
            
    # 4. 목표 층(k층)까지 다 덮어씌워졌다면, 맨 마지막 방(n호)의 인원을 출력합니다.
    print(people[-1])