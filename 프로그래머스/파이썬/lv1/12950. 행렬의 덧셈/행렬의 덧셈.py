def solution(arr1, arr2):
    row_len = len(arr1)
    col_len = len(arr1[0])
    
    # 결과를 담을 빈 행렬 초기화
    answer = []
    
    for i in range(row_len):
        row = []
        for j in range(col_len):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
        
    return answer