def solution(s):
    # 1. 공백을 기준으로 문자열을 쪼개어 리스트로 만듭니다.
    # 예: "1 -2 3" -> ["1", "-2", "3"]
    num_list = s.split()
    
    # 2. 첫 번째 값을 정수로 변환하여 초기 기준으로 잡습니다.
    max_val = int(num_list[0])
    min_val = int(num_list[0])
    
    # 3. 리스트를 돌면서 하나씩 크기를 비교합니다.
    for num_str in num_list:
        num = int(num_str)  # 비교를 위해 현재 값을 정수로 변환
        
        # 현재 숫자가 지금까지의 최대값보다 크면 업데이트
        if num > max_val:
            max_val = num
            
        # 현재 숫자가 지금까지의 최소값보다 작으면 업데이트
        if num < min_val:
            min_val = num
            
    # 4. 최종적으로 찾은 최소값과 최대값을 문자열로 합쳐서 반환합니다.
    return f"{min_val} {max_val}"