def solution(X, y):
    # 0부터 9까지 숫자의 빈도를 저장할 배열 (인덱스가 곧 숫자)
    count_X = [0] * 10
    count_Y = [0] * 10
    
    # 각 문자열의 숫자 빈도 측정
    for char in X:
        count_X[int(char)] += 1
    for char in y:
        count_Y[int(char)] += 1
        
    result = []
    
    # 가장 큰 수를 만들어야 하므로 9부터 0까지 거꾸로 순회
    for i in range(9, -1, -1):
        # 공통으로 짝지을 수 있는 개수는 두 빈도 중 최솟값
        common_count = min(count_X[i], count_Y[i])
        if common_count > 0:
            result.append(str(i) * common_count)
            
    # 리스트에 모인 문자열을 하나로 합침
    answer = "".join(result)
    
    # 예외 처리
    if not answer:
        return "-1"
    if answer[0] == "0": # 9부터 내려왔는데 첫 글자가 0이면 전체가 0으로만 이루어진 것
        return "0"
        
    return answer