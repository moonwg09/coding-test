def solution(clothes):
    clothes_dict = {}
    for name, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = []
        clothes_dict[category].append(name)

    answer = 1
    for category in clothes_dict:
        count = len(clothes_dict[category])
        answer *= (count + 1)
    
    return answer - 1