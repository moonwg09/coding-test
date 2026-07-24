def solution(x):
    sum = 0
    answer = str(x)
    for n in answer:
        sum += int(n)
    if x % sum == 0:
        return True
    else:
        return False



