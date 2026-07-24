def solution(n):
    divisor = []
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    for n in divisor:
        sum += n
    return sum