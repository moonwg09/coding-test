def solution(arr):
    answer = []
    if len(arr) == 1 : 
        answer.append(-1)
        return answer
    else:
        min = arr[0]
        for num in arr:
            if num < min:
                min = num
        arr.pop(arr.index(min))
        answer = arr
        return answer