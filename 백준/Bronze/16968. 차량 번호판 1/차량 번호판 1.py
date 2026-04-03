

str_list = list(input())
total = 1
for i in range(len(str_list)):
    # 1. 첫 번째 글자일 때 (앞글자와 비교할 필요 없음)
    if i == 0:
        if str_list[i] == 'c':
            total *= 26
        else: # 'd'일 때
            total *= 10
            
    # 2. 두 번째 글자부터 (바로 앞글자와 비교)
    else:
        # 지금 글자가 앞글자와 똑같을 때 (1가지 경우의 수 제외)
        if str_list[i] == str_list[i-1]:
            if str_list[i] == 'c':
                total *= 25
            else:
                total *= 9
        # 지금 글자가 앞글자와 다를 때 (모든 경우의 수 곱함)
        else:
            if str_list[i] == 'c':
                total *= 26
            else:
                total *= 10

print(total)





