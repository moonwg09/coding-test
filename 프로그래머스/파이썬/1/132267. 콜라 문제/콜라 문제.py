def solution(a, b, n):
    answer = []
    sum_answer = 0
    while n >= a: 
        s = n//a
        new_cola = s * b
        n = n - (a * (n//a)) + new_cola
        answer.append(new_cola)
    for value in answer:
        sum_answer += value
    return sum_answer