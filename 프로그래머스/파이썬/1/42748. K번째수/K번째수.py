def solution(array, commands):
    answer = []
    
    for command in commands:
        # 문제의 인덱스는 1부터 시작하므로, 파이썬 인덱스(0부터 시작)에 맞게 조정
        i, j, k = command
        
        # array의 i-1번째부터 j번째까지 자르기
        sliced_array = array[i-1:j]
        
        # 정렬하기
        sliced_array.sort()
        
        # k-1번째에 있는 수 가져오기
        answer.append(sliced_array[k-1])
        
    return answer