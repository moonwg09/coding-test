import sys
input = sys.stdin.readline

# 1. 소수 판별 함수
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 2. 소수 리스트 만들기
all_primes = []
for i in range(2, 320000):
    if is_prime(i):
        all_primes.append(i)

# 3. 슈퍼 소수만 골라내기
super_primes = []
for i in range(len(all_primes)):
    # i + 1 번째라는 숫자가 소수라면, 그 위치의 소수는 슈퍼 소수
    if is_prime(i + 1):
        super_primes.append(all_primes[i])

t = int(input())
for _ in range(t):
    n = int(input())
    # n번째 슈퍼 소수 출력 (인덱스는 n-1)
    print(super_primes[n-1])
    