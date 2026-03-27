import sys
import math

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))

# 1. 주어진 숫자들의 최대공약수(GCD) 구하기
if n == 2:
    g = math.gcd(numlist[0], numlist[1])
else:
    # 숫자가 3개일 때는 앞의 두 개의 GCD를 구하고, 그 결과와 세 번째 숫자의 GCD를 구합니다.
    g = math.gcd(numlist[0], math.gcd(numlist[1], numlist[2]))

# 2. 최대공약수의 약수들을 빠르게 구하기
divisors = set()
# int(g**0.5)는 g의 제곱근(루트)을 정수로 바꾼 것입니다.
for i in range(1, int(g**0.5) + 1):
    if g % i == 0:
        divisors.add(i)          # i가 약수라면 추가
        divisors.add(g // i)     # i의 짝꿍(몫)도 약수이므로 동시에 추가

# 3. 약수들을 오름차순으로 정렬하여 출력하기
for d in sorted(divisors):
    print(d)