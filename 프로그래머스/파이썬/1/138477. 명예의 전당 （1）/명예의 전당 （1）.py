import heapq

def solution(k, score):
    answer = []
    hall_of_fame = []  # 명예의 전당을 유지할 최소 힙
    
    for s in score:
        heapq.heappush(hall_of_fame, s)  # 일단 오늘 점수를 명예의 전당에 추가
        
        # 명예의 전당 정원이 초과되면 가장 낮은 점수 탈락
        if len(hall_of_fame) > k:
            heapq.heappop(hall_of_fame)
            
        # 현재 명예의 전당의 최하위 점수(가장 작은 값)를 기록
        answer.append(hall_of_fame[0])
        
    return answer