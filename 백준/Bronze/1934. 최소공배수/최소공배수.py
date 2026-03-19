# 최소공배수

def get_lcm(M, N):
    if M > N : M,N = N,M

    i = 1
    while True:
        multiple = N * i
        if multiple % M == 0:
            return multiple
        i+=1

num = int(input())
for _ in range(num):
    a, b = map(int, input().split())
    print(get_lcm(a,b))
