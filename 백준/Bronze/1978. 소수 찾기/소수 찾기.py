# 소수

def is_prime_number(N):
    if N == 1: return False
    if N == 2: return True
    for i in range(2,N):
        if N % i == 0:
            return False
    return True

count = 0
num = int(input())


primelist = (list(map(int,input().split())))
    

for number in primelist:
    if is_prime_number(number) == True:
        count +=1
    


print(count)
