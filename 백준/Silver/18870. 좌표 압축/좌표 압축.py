import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

set_list = sorted(set(num_list))

dic = {value:index for index, value in enumerate(set_list)}

for num in num_list:
    print(dic[num], end=" ")