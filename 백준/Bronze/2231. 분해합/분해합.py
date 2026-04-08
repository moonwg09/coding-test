n = int(input())

# 생성자가 될 수 있는 후보는 1부터 n 사이의 숫자입니다.
for i in range(1, n + 1):
    # i의 각 자릿수를 더하는 파이썬다운 방법!
    # 숫자를 문자열로 바꾸고(str), 다시 숫자로 바꿔서(int) 리스트로 만든 뒤 합칩니다(sum).
    digit_sum = sum(map(int, str(i)))
    
    # 분해합 = 자기 자신(i) + 자릿수의 합
    total = i + digit_sum
    
    # 만약 계산한 분해합이 입력받은 n과 같다면?
    if total == n:
        print(i) # 가장 작은 것부터 찾았으므로 바로 출력!
        break
else:
    # 1부터 n까지 다 돌았는데 break를 못 만났다면 생성자가 없는 것
    print(0)