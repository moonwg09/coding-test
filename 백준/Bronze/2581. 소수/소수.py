
num1 = int(input())
num2 = int(input())

prime = []

for i in range(num1, num2 + 1):
    # 1. 1은 소수가 아니므로 무조건 1보다 클 때만 검사합니다.
    if i > 1:
        is_prime = True  # "이 숫자는 소수일 거야!" 라고 깃발을 들어둡니다.
        
        for j in range(2, i):
            # 2. 만약 한 번이라도 나누어 떨어지면?
            if i % j == 0:
                is_prime = False  # "앗, 소수가 아니네!" 하고 깃발을 내립니다.
                break             # 더 이상 검사할 필요 없으니 반복문을 탈출!
                
        # 3. j 반복문이 끝난 후, 깃발이 여전히 올라가 있다면(True) 진짜 소수입니다!
        if is_prime:
            prime.append(i)

# 4. 리스트가 비어있으면(소수가 없으면) -1 출력
if len(prime) == 0:
    print(-1)
else:
    # 파이썬의 강력한 내장 함수 sum()과 min()을 사용하면 for문 없이 한 줄로 끝납니다!
    print(sum(prime))
    print(min(prime))