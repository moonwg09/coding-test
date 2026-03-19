#i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램


#M = 5
#N = 10
#A = [1, 2, 3, 4, 2, 5, 3, 1, 1, 2]

N, M = map(int,input().split())
A = list(map(int,input().split()))

# 정답 데이터 초기화
count = 0

# 알고리즘의 시작값 초기화
start = end = 0
sum = A[0]

while end < N:
    # 할 일 하기
    if sum == M: count += 1
    
    # 다음을 위한 조건 데이터 수정하기
    if sum > M:
        sum -= A[start]
        start += 1
    else:
        end += 1
        if end < N: sum += A[end]

print(count)
