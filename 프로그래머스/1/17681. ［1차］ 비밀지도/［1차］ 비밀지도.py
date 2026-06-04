def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 1. 두 지도의 같은 행을 비트 OR 연산합니다.
        # 2. bin() 함수로 이진수 문자열로 변환합니다. (앞에 '0b'가 붙음)
        # 3. [2:]로 '0b'를 잘라냅니다.
        # 4. zfill(n)을 사용해 n자리가 되도록 앞에 '0'을 채웁니다.
        binary_str = bin(arr1[i] | arr2[i])[2:].zfill(n)
        
        # 5. '1'은 '#'으로, '0'은 공백으로 치환합니다.
        row = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(row)
        
    return answer