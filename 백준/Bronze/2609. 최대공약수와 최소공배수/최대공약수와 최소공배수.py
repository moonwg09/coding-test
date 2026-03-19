
# 최대 공약수 구하기

def get_gcd(M, N):
    if M > N : M, N = N, M

    for num in range(M,0,-1):
        if M % num == 0 and N % num == 0:
            return num

# 최소공배수

def get_lcm(M, N):
    if M > N : M,N = N,M

    i = 1
    while True:
        multiple = N * i
        if multiple % M == 0:
            return multiple
        i+=1

num1,num2 = map(int, input().split())

print(get_gcd(num1,num2))
print(get_lcm(num1,num2))


