
n = int(input())

num_list = []

for _ in range(n):
    num_list.append(int(input()))

set_list = sorted(set(num_list))

for num in set_list:
    print(num)