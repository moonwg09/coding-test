def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += (price*i)
    answer = sum - money
    
    if answer <= 0:
        return 0
    else:
        return answer
    
   