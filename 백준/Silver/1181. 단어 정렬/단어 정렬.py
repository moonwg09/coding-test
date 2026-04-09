
n = int(input())

str_list = []

for _ in range(n):
    str = input()
    str_list.append(str)

str_list.sort()
str_list = sorted(str_list, key=len)

unique_list = list(dict.fromkeys(str_list)) # 중복 제거

for str in unique_list:
    print(str)

