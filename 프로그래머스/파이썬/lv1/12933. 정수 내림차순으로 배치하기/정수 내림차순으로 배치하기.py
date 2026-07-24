def solution(n):
    num_list = [int(s) for s in str(n)]
    num_list.sort(reverse=True)
    result = int(''.join(map(str, num_list)))
    return result