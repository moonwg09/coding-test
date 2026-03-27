# 1. 소수인지 판별해 주는 자판기(함수)를 만듭니다.
def is_prime(n):
    if n < 2:
        return False
    
    # 시간 초과를 막기 위해 숫자의 제곱근(루트)까지만 나누어 봅니다.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # 한 번이라도 나누어 떨어지면 소수가 아님 (자판기 종료)
            
    return True  # 무사히 반복문을 다 통과하면 소수! (자판기 종료)

# 2. 기존 6자리 번호와 추가할 1자리 번호를 문자열로 입력받습니다.
original, new_digit = input().split()

# 3. 기존 번호와, 문자열을 더해서 만든 새로운 7자리 번호를 정수(int)로 바꿉니다.
num1 = int(original)
num2 = int(new_digit + original)

# 4. 만들어둔 함수에 두 숫자를 넣어서 둘 다 소수(True)인지 확인합니다.
if is_prime(num1) and is_prime(num2):
    print("Yes")
else:
    print("No")



